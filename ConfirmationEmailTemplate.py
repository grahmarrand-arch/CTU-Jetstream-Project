# Generates confirmation email text for Jetstream Airlines.
# This module only builds the email body; it does not send emails.

class ConfirmationEmailTemplate:
    # Encapsulates logic for generating confirmation emails.
    # Keeping templates centralized ensures consistent formatting.

    def generate_email(
        self,
        passenger_name: str,
        flight_number: str,
        departure: str,
        destination: str,
        date: str,
        seat_class: str,
        total_fare: float
    ) -> str:
        # Generates a formatted confirmation email using f-string assembly.
        # All formatting is done with simple string concatenation to avoid
        # multi-line triple-quoted blocks that Render may misinterpret.

        lines = []
        lines.append(f"Dear {passenger_name},")
        lines.append("")
        lines.append("Thank you for booking with Jetstream Airlines!")
        lines.append("Your reservation has been successfully confirmed.")
        lines.append("")
        lines.append("BOOKING DETAILS")
        lines.append("------------------------------")
        lines.append(f"Flight Number: {flight_number}")
        lines.append(f"From: {departure}")
        lines.append(f"To: {destination}")
        lines.append(f"Date: {date}")
        lines.append(f"Seat Class: {seat_class}")
        lines.append(f"Total Fare: ${total_fare:.2f}")
        lines.append("")
        lines.append("We look forward to providing you with a smooth and enjoyable travel experience.")
        lines.append("")
        lines.append("Safe travels,")
        lines.append("Jetstream Airlines")

        # Join lines into a single email body string
        return "\n".join(lines)
