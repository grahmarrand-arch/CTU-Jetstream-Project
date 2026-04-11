from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

# -----------------------------------
# Initialize App
# -----------------------------------
app = FastAPI(title="Flight Seat Availability API")

# -----------------------------------
# In-memory Database
# -----------------------------------
seat_db: Dict[str, List[dict]] = {
    "FL001": [
        {"seat_number": "1A", "is_booked": False},
        {"seat_number": "1B", "is_booked": True},
        {"seat_number": "1C", "is_booked": False},
        {"seat_number": "2A", "is_booked": False},
        {"seat_number": "2B", "is_booked": True},
    ],
    "FL002": [
        {"seat_number": "1A", "is_booked": False},
        {"seat_number": "1B", "is_booked": False},
        {"seat_number": "1C", "is_booked": False},
    ]
}

# -----------------------------------
# Request Models
# -----------------------------------
class ReserveRequest(BaseModel):
    seat_number: str

# -----------------------------------
# Helper Functions
# -----------------------------------
def get_flight(flight_id: str):
    return seat_db.get(flight_id)

def find_seat(flight_id: str, seat_number: str):
    seats = seat_db.get(flight_id)
    if not seats:
        return None

    for seat in seats:
        if seat["seat_number"] == seat_number:
            return seat
    return None

# -----------------------------------
# API: Get Seat Availability
# -----------------------------------
@app.get("/flights/{flight_id}/seats")
def get_seats(flight_id: str):
    seats = get_flight(flight_id)

    if seats is None:
        raise HTTPException(status_code=404, detail="Flight not found")

    return {
        "flight_id": flight_id,
        "seats": seats
    }

# -----------------------------------
# API: Reserve Seat
# -----------------------------------
@app.post("/flights/{flight_id}/reserve")
def reserve_seat(flight_id: str, request: ReserveRequest):
    seat = find_seat(flight_id, request.seat_number)

    if seat is None:
        raise HTTPException(status_code=404, detail="Seat or flight not found")

    if seat["is_booked"]:
        raise HTTPException(status_code=400, detail="Seat already booked")

    seat["is_booked"] = True

    return {
        "message": "Seat reserved successfully",
        "flight_id": flight_id,
        "seat_number": request.seat_number
    }

# -----------------------------------
# API: Reset Seat (for testing)
# -----------------------------------
@app.post("/flights/{flight_id}/reset/{seat_number}")
def reset_seat(flight_id: str, seat_number: str):
    seat = find_seat(flight_id, seat_number)

    if seat is None:
        raise HTTPException(status_code=404, detail="Seat not found")

    seat["is_booked"] = False

    return {
        "message": "Seat reset successfully",
        "seat_number": seat_number
    }