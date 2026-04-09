"""
confirmation_email_template.py
------------------------------
This standalone module generates a confirmation email template for Jetstream LLC.

It is fully commented and designed to integrate into any Python backend.
The template is dynamic — booking details are inserted at runtime.

This module does NOT send emails; it only generates the email body.
A separate email-sending module can import and use this.
"""

class ConfirmationEmailTemplate:
    """
    Encapsulates all logic for generating confirmation emails.
    Keeping templates centralized ensures consistent branding and formatting.
    """

    def generate_email(self, passenger_name: str, flight_number: str,
                       departure: str, destination: str, date: str,
                       seat_class: str, total_fare: float) -> str:
        """
        Generates a formatted confirmation email.

        Parameters:
            passenger_name: Name of the passenger
            flight_number: Jetstream flight identifier
            departure: Departure airport/city
            destination: Destination airport/city
            date: Flight date
            seat_class: Selected seat class
            total_fare: Final fare after calculations

        Returns:
            A string containing the full email body.
        """

        # Build the email body using f-string formatting
        email_body = f"""
        Dear {passenger_name},

        Thank you for booking with Jetstream Airlines!
        Your reservation has been successfully confirmed.

        ------------------------------
        BOOKING DETAILS
        ------------------------------
        Flight Number: {flight_number}
        From: {departure}
        To: {destination}
        Date: {date}
        Seat Class: {seat_class}
        Total Fare: ${total_fare:.2f}

        We look forward to providing you with a smooth and enjoyable travel experience.

        Safe travels,
        Jetstream Airlines
        """

        # Return the final email text
        return email_body.strip()
