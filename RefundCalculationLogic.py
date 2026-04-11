from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Booking:
    booking_id: str
    amount_paid: float
    departure_time: datetime
    booking_time: datetime
    is_cancelled: bool = False


@dataclass
class RefundPolicy:
    full_refund_hours_before: int = 24     # full refund if cancelled before X hours
    partial_refund_hours_before: int = 6   # partial refund window
    partial_refund_percent: float = 50.0   # % refund in partial window
    cancellation_fee: float = 10.0         # fixed fee


class RefundCalculator:
    def __init__(self, policy: RefundPolicy):
        self.policy = policy

    def calculate_refund(self, booking: Booking, cancel_time: datetime) -> dict:
        if not booking.is_cancelled:
            booking.is_cancelled = True

        time_to_departure = booking.departure_time - cancel_time
        hours_before = time_to_departure.total_seconds() / 3600

        refund_amount = 0.0
        reason = ""

        # Case 1: Full refund
        if hours_before >= self.policy.full_refund_hours_before:
            refund_amount = booking.amount_paid
            reason = "Full refund (early cancellation)"

        # Case 2: Partial refund
        elif hours_before >= self.policy.partial_refund_hours_before:
            refund_amount = booking.amount_paid * (self.policy.partial_refund_percent / 100)
            refund_amount -= self.policy.cancellation_fee
            reason = "Partial refund (moderate cancellation window)"

        # Case 3: No refund
        else:
            refund_amount = 0.0
            reason = "No refund (late cancellation)"

        # Ensure refund is not negative
        refund_amount = max(0.0, round(refund_amount, 2))

        return {
            "booking_id": booking.booking_id,
            "refund_amount": refund_amount,
            "original_amount": booking.amount_paid,
            "reason": reason,
            "cancel_time": cancel_time.isoformat(),
            "departure_time": booking.departure_time.isoformat()
        }


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    policy = RefundPolicy()

    calculator = RefundCalculator(policy)

    booking = Booking(
        booking_id="BK123",
        amount_paid=200.0,
        booking_time=datetime.now() - timedelta(days=2),
        departure_time=datetime.now() + timedelta(hours=20)
    )

    cancel_time = datetime.now()

    result = calculator.calculate_refund(booking, cancel_time)

    print(result)