# Payment success and failure handler for Jetstream.
# Render-safe version with simple comments.

from confirmation_messages import success_message, error_message


class PaymentHandler:
    # Handles payment result processing.

    def __init__(self, logger=None):
        self.logger = logger

    def payment_success(self, amount: float, card_type: str) -> dict:
        message = f"Payment of ${amount:.2f} approved using {card_type}."
        if self.logger:
            self.logger.info(f"[PAYMENT SUCCESS] {message}")
        return success_message(message)

    def payment_failure(self, reason: str) -> dict:
        if self.logger:
            self.logger.error(f"[PAYMENT FAILURE] {reason}")
        return error_message(f"Payment failed: {reason}")
