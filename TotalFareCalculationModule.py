"""
fare_calculator.py
------------------
This standalone module calculates the total fare for a Jetstream passenger.

It is fully commented and designed to be integrated into any Python backend.

The calculation includes:
- Base fare (from flight database)
- Seat class multiplier
- Taxes
- Service fees
"""

class FareCalculator:
    """
    FareCalculator encapsulates all fare-related logic.
    This keeps pricing rules centralized and easy to update.
    """

    def __init__(self):
        """
        Constructor initializes seat class multipliers.
        These values can be adjusted based on Jetstream's pricing policy.
        """
        self.class_multipliers = {
            "Economy": 1.0,
            "Premium Economy": 1.3,
            "Business": 1.8,
            "First Class": 2.5
        }

        # Default tax and service fee percentages
        self.tax_rate = 0.07       # 7% tax
        self.service_fee = 25.00   # Flat service fee in USD

    def calculate_total_fare(self, base_fare: float, seat_class: str) -> float:
        """
        Calculates the total fare for a passenger.

        Steps:
        1. Apply seat class multiplier
        2. Add tax
        3. Add service fee

        Returns:
            Total fare as a float
        """

        # --- Step 1: Apply seat class multiplier ---
        multiplier = self.class_multipliers.get(seat_class, 1.0)
        fare_after_class = base_fare * multiplier

        # --- Step 2: Apply tax ---
        tax_amount = fare_after_class * self.tax_rate

        # --- Step 3: Add service fee ---
        total_fare = fare_after_class + tax_amount + self.service_fee

        return round(total_fare, 2)
