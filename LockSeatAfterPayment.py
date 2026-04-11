from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from datetime import datetime, timedelta
import threading
import time

app = FastAPI()

# -----------------------------
# In-memory "database"
# -----------------------------
class Seat:
    def __init__(self, seat_id):
        self.seat_id = seat_id
        self.status = "available"   # available | reserved | booked
        self.user_id = None
        self.lock_expiry = None


seats_db = {f"A{i}": Seat(f"A{i}") for i in range(1, 11)}  # 10 seats


# -----------------------------
# Request models
# -----------------------------
class ReserveRequest(BaseModel):
    seat_id: str
    user_id: str


class PaymentRequest(BaseModel):
    seat_id: str
    user_id: str


# -----------------------------
# Core logic
# -----------------------------
def reserve_seat(seat: Seat, user_id: str):
    if seat.status != "available":
        return False, "Seat not available"

    seat.status = "reserved"
    seat.user_id = user_id
    seat.lock_expiry = datetime.now() + timedelta(minutes=2)

    return True, "Seat reserved for 2 minutes"


def confirm_booking(seat: Seat, user_id: str):
    if seat.status != "reserved":
        return False, "Seat not reserved"

    if seat.user_id != user_id:
        return False, "User mismatch"

    seat.status = "booked"
    seat.lock_expiry = None

    return True, "Seat booked successfully"


def release_seat(seat: Seat):
    seat.status = "available"
    seat.user_id = None
    seat.lock_expiry = None


# -----------------------------
# Background cleanup thread
# -----------------------------
def cleanup_task():
    while True:
        now = datetime.now()
        for seat in seats_db.values():
            if seat.status == "reserved" and seat.lock_expiry and seat.lock_expiry < now:
                print(f"[AUTO-RELEASE] Seat {seat.seat_id} expired")
                release_seat(seat)
        time.sleep(5)


threading.Thread(target=cleanup_task, daemon=True).start()


# -----------------------------
# API Endpoints
# -----------------------------

@app.get("/seats")
def get_seats():
    return {
        seat_id: {
            "status": seat.status,
            "user_id": seat.user_id,
            "expires": str(seat.lock_expiry) if seat.lock_expiry else None
        }
        for seat_id, seat in seats_db.items()
    }


@app.post("/reserve")
def reserve(req: ReserveRequest):
    seat = seats_db.get(req.seat_id)
    if not seat:
        return {"error": "Seat not found"}

    success, msg = reserve_seat(seat, req.user_id)
    return {"success": success, "message": msg}


@app.post("/payment/success")
def payment_success(req: PaymentRequest):
    seat = seats_db.get(req.seat_id)
    if not seat:
        return {"error": "Seat not found"}

    success, msg = confirm_booking(seat, req.user_id)
    return {"success": success, "message": msg}


@app.post("/release")
def manual_release(req: PaymentRequest):
    seat = seats_db.get(req.seat_id)
    if not seat:
        return {"error": "Seat not found"}

    release_seat(seat)
    return {"message": "Seat released"}