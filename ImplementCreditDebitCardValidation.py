# Credit/debit card validator for Jetstream.

from datetime import datetime


class CardValidator:
    # Validates card number, expiration, CVV, and type.

    def __init__(self):
        self.card_types = {
            "Visa": ["4"],
            "MasterCard": ["51", "52", "53", "54", "55"],
            "American Express": ["34", "37"],
            "Discover": ["6011", "65"]
        }

    def luhn_check(self, card_number: str) -> bool:
        # Validates card number using Luhn algorithm.

        card_number = card_number.replace(" ", "").replace("-", "")
        if not card_number.isdigit():
            return False

        total = 0
        reverse_digits = card_number[::-1]

        for i, digit in enumerate(reverse_digits):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n

        return total % 10 == 0

    def detect_card_type(self, card_number: str) -> str:
        # Determines card type based on prefixes.

        for card_type, prefixes in self.card_types.items():
            for prefix in prefixes:
                if card_number.startswith(prefix):
                    return card_type
        return "Unknown"

    def validate_expiration(self, month: int, year: int) -> bool:
        # Checks if expiration date is valid.

        if year < 100:
            year += 2000

        now = datetime.now()
        exp_date = datetime(year, month, 1)

        return exp_date >= datetime(now.year, now.month, 1)

    def validate_cvv(self, cvv: str, card_type: str) -> bool:
        # Validates CVV format.

        if not cvv.isdigit():
            return False

        if card_type == "American Express":
            return len(cvv) == 4

        return len(cvv) == 3

    def validate_card(self, card_number: str, exp_month: int, exp_year: int, cvv: str) -> dict:
        # Full validation wrapper.

        card_type = self.detect_card_type(card_number)

        if not self.luhn_check(card_number):
            return {"valid": False, "card_type": card_type, "message": "Invalid card number."}

        if not self.validate_expiration(exp_month, exp_year):
            return {"valid": False, "card_type": card_type, "message": "Card is expired."}

        if not self.validate_cvv(cvv, card_type):
            return {"valid": False, "card_type": card_type, "message": "Invalid CVV format."}

        return {"valid": True, "card_type": card_type, "message": "Card is valid."}
