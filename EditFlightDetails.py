from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Flight:
    flight_id: str
    airline: str
    departure: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    price: float
    available_seats: int


class FlightDatabase:
    def __init__(self):
        self.flights = {}  # flight_id -> Flight

    def add_flight(self, flight: Flight):
        self.flights[flight.flight_id] = flight

    def edit_flight(
        self,
        flight_id: str,
        price: Optional[float] = None,
        departure_time: Optional[datetime] = None,
        arrival_time: Optional[datetime] = None,
        available_seats: Optional[int] = None
    ):
        """
        Edit flight details: price, time, seats
        """
        if flight_id not in self.flights:
            return f"Flight {flight_id} not found"

        flight = self.flights[flight_id]

        if price is not None:
            flight.price = price

        if departure_time is not None:
            flight.departure_time = departure_time

        if arrival_time is not None:
            flight.arrival_time = arrival_time

        if available_seats is not None:
            if available_seats < 0:
                return "Seats cannot be negative"
            flight.available_seats = available_seats

        self.flights[flight_id] = flight
        return f"Flight {flight_id} updated successfully"


# Example usage
db = FlightDatabase()

db.add_flight(Flight(
    flight_id="FL123",
    airline="Delta",
    departure="NYC",
    destination="LAX",
    departure_time=datetime(2026, 4, 12, 9, 0),
    arrival_time=datetime(2026, 4, 12, 12, 0),
    price=300.0,
    available_seats=120
))

# Edit flight details
result = db.edit_flight(
    "FL123",
    price=350.0,
    available_seats=100
)

print(result)