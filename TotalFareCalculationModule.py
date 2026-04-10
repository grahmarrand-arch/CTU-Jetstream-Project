# Fare calculation module for Jetstream.
# Render-safe version with simple comments.

class FareCalculator:
    # Handles fare calculation logic.

    def __init__(self):
        self.class_multipliers = {
            "Economy": 1.0,
            "Premium Economy": 1.3,
            "Business": 1.8,
            "First Class": 2.5
        }

        self.tax_rate = 0.07
        self.service_fee = 25.00

    def calculate_total_fare(self, base_fare: float, seat_class: str) -> float:
        # Applies seat class multiplier, tax, and service fee.

        multiplier = self.class_multipliers.get(seat_class, 1.0)
        fare_after_class = base_fare * multiplier
        tax_amount = fare_after_class * self.tax_rate
        total_fare = fare_after_class + tax_amount + self.service_fee

        return round(total_fare, 2)
