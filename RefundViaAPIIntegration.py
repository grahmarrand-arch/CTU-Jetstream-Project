from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

# -----------------------------
# Mock Database (in-memory)
# -----------------------------
BOOKINGS = {
    "B001": {
        "booking_id": "B001",
        "payment_id": "PAY123",
        "seat": "12A",
        "price": 200.0,
        "status": "CONFIRMED",
        "refund_status": "NONE"
    }
}

# -----------------------------
# Config (Payment Gateway)
# -----------------------------
PAYMENT_API_URL = "https://api.paymentgateway.com/v1/refunds"
API_KEY = "your_api_key_here"


# -----------------------------
# Payment Refund Function
# -----------------------------
def trigger_refund(payment_id: str, amount: float):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "payment_id": payment_id,
        "amount": int(amount * 100)  # cents
    }

    try:
        response = requests.post(PAYMENT_API_URL, json=payload, headers=headers)

        if response.status_code == 200:
            return {"status": "success", "data": response.json()}

        return {"status": "failed", "error": response.text}

    except Exception as e:
        return {"status": "error", "error": str(e)}


# -----------------------------
# Cancel Booking + Refund
# -----------------------------
@app.post("/cancel/{booking_id}")
def cancel_booking(booking_id: str):
    booking = BOOKINGS.get(booking_id)

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    if booking["status"] == "CANCELLED":
        return {"message": "Booking already cancelled"}

    # Refund policy (example: 80%)
    refund_amount = booking["price"] * 0.8

    refund_result = trigger_refund(
        payment_id=booking["payment_id"],
        amount=refund_amount
    )

    if refund_result["status"] != "success":
        raise HTTPException(status_code=500, detail="Refund failed")

    # Update booking
    booking["status"] = "CANCELLED"
    booking["refund_status"] = "REFUNDED"

    return {
        "message": "Booking cancelled successfully",
        "booking_id": booking_id,
        "refund_amount": refund_amount,
        "seat_released": booking["seat"],
        "refund_response": refund_result["data"]
    }


# -----------------------------
# Run:
# uvicorn app:app --reload
# -----------------------------