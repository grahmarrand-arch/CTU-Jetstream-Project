import time
import uuid
from dataclasses import dataclass
from typing import List, Dict


# -----------------------------
# Data Models
# -----------------------------

@dataclass
class FlightLeg:
    flight_id: str
    price: float


@dataclass
class Itinerary:
    itinerary_id: str
    legs: List[FlightLeg]
    status: str = "DRAFT"


@dataclass
class PaymentIntent:
    payment_intent_id: str
    itinerary_id: str
    amount: float
    currency: str = "USD"
    status: str = "PENDING"
    lock_token: str = ""
    booking_id: str = None


# -----------------------------
# Pricing Engine
# -----------------------------

class PricingService:

    def calculate_total(self, legs: List[FlightLeg], addons: float = 0.0) -> float:
        base = sum(l.price for l in legs)
        subtotal = base + addons

        discount = self.apply_discount(legs, subtotal)
        taxable = subtotal - discount

        tax = taxable * 0.08  # 8% tax

        return round(taxable + tax, 2)

    def apply_discount(self, legs, subtotal):
        if len(legs) >= 3:
            return subtotal * 0.05  # 5% discount for multi-leg
        return 0.0


# -----------------------------
# Lock Service (Price/Seat Lock)
# -----------------------------

class LockService:

    def __init__(self):
        self.locks: Dict[str, float] = {}

    def create_lock(self, ttl_seconds=900):
        token = str(uuid.uuid4())
        self.locks[token] = time.time() + ttl_seconds
        return token

    def validate_lock(self, token: str) -> bool:
        return token in self.locks and time.time() < self.locks[token]

    def release_lock(self, token: str):
        if token in self.locks:
            del self.locks[token]


# -----------------------------
# Payment Gateway (Mock)
# -----------------------------

class PaymentGateway:

    def charge(self, amount: float) -> bool:
        # simulate success/failure
        return amount > 0


# -----------------------------
# Booking Service (Core Logic)
# -----------------------------

class BookingService:

    def __init__(self):
        self.pricing = PricingService()
        self.locks = LockService()
        self.gateway = PaymentGateway()
        self.bookings: Dict[str, dict] = {}

    def create_itinerary(self, legs: List[FlightLeg]) -> Itinerary:
        return Itinerary(
            itinerary_id=str(uuid.uuid4()),
            legs=legs
        )

    def initiate_payment(self, itinerary: Itinerary, addons: float = 0.0) -> PaymentIntent:
        amount = self.pricing.calculate_total(itinerary.legs, addons)
        lock_token = self.locks.create_lock()

        return PaymentIntent(
            payment_intent_id=str(uuid.uuid4()),
            itinerary_id=itinerary.itinerary_id,
            amount=amount,
            lock_token=lock_token,
            status="AWAITING_PAYMENT"
        )

    def confirm_payment(self, payment: PaymentIntent):

        # Validate lock
        if not self.locks.validate_lock(payment.lock_token):
            payment.status = "LOCK_EXPIRED"
            return payment

        # Charge payment
        success = self.gateway.charge(payment.amount)

        if not success:
            payment.status = "FAILED"
            self.locks.release_lock(payment.lock_token)
            return payment

        # Success path
        payment.status = "PAID"
        booking_id = self.finalize_booking(payment)
        payment.booking_id = booking_id

        self.locks.release_lock(payment.lock_token)
        return payment

    def finalize_booking(self, payment: PaymentIntent) -> str:
        booking_id = str(uuid.uuid4())

        self.bookings[booking_id] = {
            "itinerary_id": payment.itinerary_id,
            "amount_paid": payment.amount,
            "status": "CONFIRMED"
        }

        return booking_id


# -----------------------------
# Refund Service
# -----------------------------

class RefundService:

    def refund(self, booking_service: BookingService, booking_id: str):

        if booking_id not in booking_service.bookings:
            return {"status": "NOT_FOUND"}

        booking_service.bookings[booking_id]["status"] = "REFUNDED"

        return {
            "status": "REFUNDED",
            "booking_id": booking_id
        }


# -----------------------------
# Example Run
# -----------------------------

if __name__ == "__main__":

    legs = [
        FlightLeg("F1", 120),
        FlightLeg("F2", 180),
        FlightLeg("F3", 150),
    ]

    service = BookingService()

    # Create itinerary
    itinerary = service.create_itinerary(legs)

    # Start payment
    payment = service.initiate_payment(itinerary, addons=40)

    print("Calculated Amount:", payment.amount)

    # Confirm payment
    result = service.confirm_payment(payment)

    print("Payment Status:", result.status)
    print("Booking ID:", result.booking_id)

    # Optional refund demo
    if result.booking_id:
        refund_service = RefundService()
        refund_result = refund_service.refund(service, result.booking_id)
        print("Refund:", refund_result)