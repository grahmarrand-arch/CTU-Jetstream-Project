"""
payment_handler.py
------------------
This standalone module handles payment success and failure responses
for Jetstream LLC's booking system.

It provides:
- Standardized success messages
- Standardized failure messages
- Optional logging hooks
"""

from confirmation_messages import success_message, error_message


class PaymentHandler:
    """
    PaymentHandler encapsulates all logic related to payment result processing.
    """

    def __init__(self, logger=None):
        """
        Optional logger can be injected for audit trails.
        If no logger is provided, logging is skipped.
        """
        self.logger = logger

    def payment_success(self, amount: float, card_type: str) -> dict:
        """
        Handles successful payment events.

        Returns a standardized success response.
        """

        message = f"Payment of ${amount:.2f} approved using {card_type}."

        # Log event if logger is available
        if self.logger:
            self.logger.info(f"[PAYMENT SUCCESS] {message}")

        return success_message(message)

    def payment_failure(self, reason: str) -> dict:
        """
        Handles failed payment events.

        Returns a standardized error response.
        """

        # Log event if logger is available
        if self.logger:
            self.logger.error(f"[PAYMENT FAILURE] {reason}")

        return error_message(f"Payment failed: {reason}")
