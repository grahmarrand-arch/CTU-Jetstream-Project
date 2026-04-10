"""

This module validates credit/debit card information for Jetstream LLC.

It performs:
- Luhn algorithm check for card number validity
- Expiration date validation
- CVV format validation
- Card type detection (Visa, MasterCard, AmEx, Discover)

This module is fully commented and designed to integrate into any Python backend.
"""

from datetime import datetime


class CardValidator:
    """
    CardValidator encapsulates all logic related to validating card details.
    Keeping this logic separate makes the payment system modular and maintainable.
    """

    def __init__(self):
        """
        Constructor initializes card type patterns.
        These patterns help identify card brands based on number prefixes.
        """
        self.card_types = {
            "Visa": ["4"],
            "MasterCard": ["51", "52", "53", "54", "55"],
            "American Express": ["34", "37"],
            "Discover": ["6011", "65"]
        }

    # ---------------------------------------------------------
    # Luhn Algorithm — Industry Standard Card Number Validation
    # ---------------------------------------------------------
    def luhn_check(self, card_number: str) -> bool:
        """
        Validates a card number using the Luhn algorithm.

        Steps:
        1. Reverse digits
        2. Double every second digit
        3. Subtract 9 if doubling > 9
        4. Sum all digits
        5. Valid if sum % 10 == 0
        """

        # Remove spaces or dashes for safety
        card_number = card_number.replace(" ", "").replace("-", "")

        # Ensure card number is numeric
        if not card_number.isdigit():
            return False

        total = 0
        reverse_digits = card_number[::-1]

        for i, digit in enumerate(reverse_digits):
            n = int(digit)

            # Double every second digit
            if i % 2 == 1:
                n *= 2
                # If doubling exceeds 9, subtract 9
                if n > 9:
                    n -= 9

            total += n

        # Valid if total ends in 0
        return total % 10 == 0

    # ---------------------------------------------------------
    # Card Type Detection
    # ---------------------------------------------------------
    def detect_card_type(self, card_number: str) -> str:
        """
        Determines the card type based on known number prefixes.
        Returns the card type name or 'Unknown'.
        """

        for card_type, prefixes in self.card_types.items():
            for prefix in prefixes:
                if card_number.startswith(prefix):
                    return card_type

        return "Unknown"

    # ---------------------------------------------------------
    # Expiration Date Validation
    # ---------------------------------------------------------
    def validate_expiration(self, month: int, year: int) -> bool:
        """
        Validates that the expiration date is not in the past.
        """

        # Convert to full year if needed (e.g., 26 → 2026)
        if year < 100:
            year += 2000

        now = datetime.now()
        exp_date = datetime(year, month, 1)

        # Valid if expiration date is this month or later
        return exp_date >= datetime(now.year, now.month, 1)

    # ---------------------------------------------------------
    # CVV Validation
    # ---------------------------------------------------------
    def validate_cvv(self, cvv: str, card_type: str) -> bool:
        """
        Validates CVV format:
        - Visa, MasterCard, Discover → 3 digits
        - American Express → 4 digits
        """

        if not cvv.isdigit():
            return False

        if card_type == "American Express":
            return len(cvv) == 4

        return len(cvv) == 3

    # ---------------------------------------------------------
    # Full Validation Wrapper
    # ---------------------------------------------------------
    def validate_card(self, card_number: str, exp_month: int, exp_year: int, cvv: str) -> dict:
        """
        Validates all card fields and returns a structured result.

        Returns:
            {
                "valid": True/False,
                "card_type": "Visa",
                "message": "Card is valid."
            }
        """

        # Detect card type
        card_type = self.detect_card_type(card_number)

        # Luhn check
        if not self.luhn_check(card_number):
            return {"valid": False, "card_type": card_type, "message": "Invalid card number."}

        # Expiration check
        if not self.validate_expiration(exp_month, exp_year):
            return {"valid": False, "card_type": card_type, "message": "Card is expired."}

        # CVV check
        if not self.validate_cvv(cvv, card_type):
            return {"valid": False, "card_type": card_type, "message": "Invalid CVV format."}

        # All checks passed
        return {"valid": True, "card_type": card_type, "message": "Card is valid."}
