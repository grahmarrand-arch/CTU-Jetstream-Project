import uuid
from typing import List, Optional


class Destination:
    def __init__(self, city: str, airport_code: str,
                 arrival_date: Optional[str] = None,
                 departure_date: Optional[str] = None):
        self.city = city
        self.airport_code = airport_code.upper()
        self.arrival_date = arrival_date
        self.departure_date = departure_date

    def __repr__(self):
        return f"{self.city}({self.airport_code})"


class Itinerary:
    def __init__(self, user_id: str):
        self.itinerary_id = str(uuid.uuid4())
        self.user_id = user_id
        self.destinations: List[Destination] = []

    # -------------------------
    # Add destination
    # -------------------------
    def add_destination(self, destination: Destination):
        self.destinations.append(destination)
        return {
            "message": "Destination added",
            "total_stops": len(self.destinations)
        }

    # -------------------------
    # Remove destination
    # -------------------------
    def remove_destination(self, airport_code: str):
        airport_code = airport_code.upper()

        before = len(self.destinations)
        self.destinations = [
            d for d in self.destinations if d.airport_code != airport_code
        ]
        after = len(self.destinations)

        return {
            "message": "Removed" if before != after else "Not found",
            "total_stops": after
        }

    # -------------------------
    # Move / reorder stop
    # -------------------------
    def move_destination(self, from_index: int, to_index: int):
        if from_index < 0 or to_index < 0:
            return {"error": "Index cannot be negative"}

        if from_index >= len(self.destinations) or to_index >= len(self.destinations):
            return {"error": "Invalid index"}

        item = self.destinations.pop(from_index)
        self.destinations.insert(to_index, item)

        return {"message": "Reordered successfully"}

    # -------------------------
    # Validate itinerary
    # -------------------------
    def validate(self):
        if len(self.destinations) == 0:
            return {"valid": False, "error": "No destinations added"}

        seen = set()

        for d in self.destinations:
            if d.airport_code in seen:
                return {
                    "valid": False,
                    "error": f"Duplicate airport detected: {d.airport_code}"
                }
            seen.add(d.airport_code)

        return {"valid": True, "message": "Itinerary is valid"}

    # -------------------------
    # Build summary
    # -------------------------
    def build_summary(self):
        if not self.destinations:
            return {"error": "Empty itinerary"}

        route = " → ".join(
            f"{d.city}({d.airport_code})" for d in self.destinations
        )

        return {
            "itinerary_id": self.itinerary_id,
            "user_id": self.user_id,
            "route": route,
            "stops": len(self.destinations)
        }

    # -------------------------
    # Pretty print (debug helper)
    # -------------------------
    def print_itinerary(self):
        print("\n=== ITINERARY ===")
        print(f"ID: {self.itinerary_id}")
        print(f"User: {self.user_id}")
        print("Route:")

        for i, d in enumerate(self.destinations):
            print(f"  {i + 1}. {d.city} ({d.airport_code})")

        print("=================\n")


# -------------------------
# Demo / Test Run
# -------------------------
if __name__ == "__main__":
    itinerary = Itinerary(user_id="USER_001")

    print(itinerary.add_destination(Destination("New York", "JFK")))
    print(itinerary.add_destination(Destination("London", "LHR")))
    print(itinerary.add_destination(Destination("Paris", "CDG")))

    itinerary.print_itinerary()

    print(itinerary.build_summary())
    print(itinerary.validate())

    print(itinerary.move_destination(2, 1))

    itinerary.print_itinerary()

    print(itinerary.remove_destination("LHR"))

    itinerary.print_itinerary()
    print(itinerary.build_summary())