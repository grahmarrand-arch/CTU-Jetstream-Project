from datetime import datetime

def validate_itinerary(trips):
    """
    trips: list of dicts with:
    {
        "from": "A",
        "to": "B",
        "departure": "2026-04-10 10:00",
        "arrival": "2026-04-10 14:00"
    }
    """

    fmt = "%Y-%m-%d %H:%M"

    parsed = []
    for t in trips:
        dep = datetime.strptime(t["departure"], fmt)
        arr = datetime.strptime(t["arrival"], fmt)

        # Rule 1: departure must be before arrival
        if dep >= arr:
            return False, f"Invalid segment {t['from']} → {t['to']}: departure >= arrival"

        parsed.append((dep, arr))

    # Rule 2: chronological continuity
    for i in range(len(parsed) - 1):
        current_arrival = parsed[i][1]
        next_departure = parsed[i + 1][0]

        if current_arrival > next_departure:
            return False, f"Overlap between segment {i} and {i+1}"

    return True, "Valid itinerary"


# Example usage
trips = [
    {"from": "NYC", "to": "LON", "departure": "2026-04-10 10:00", "arrival": "2026-04-10 20:00"},
    {"from": "LON", "to": "PAR", "departure": "2026-04-11 09:00", "arrival": "2026-04-11 11:00"},
]

print(validate_itinerary(trips))