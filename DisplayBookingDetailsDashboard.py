# Prepares booking details for display on the Jetstream dashboard.
# This module does not handle HTML rendering. It returns a clean,
# structured dictionary that any UI layer (HTML, React, mobile app)
# can consume. 

class DashboardBookingDisplay:
    # Encapsulates logic for formatting booking details for dashboard display.

    def format_booking(self, booking_record: dict) -> dict:
        # Accepts a booking record (from database or API) and formats it
        # into a clean structure for the dashboard.
        #
        # booking_record is expected to contain:
        # - passenger_name
        # - flight_number
        # - departure
        # - destination
        # - date
        # - seat_class
        # - total_fare

        # Extract fields safely using .get() to avoid KeyErrors.
        formatted = {
            "Passenger Name": booking_record.get("passenger_name", "N/A"),
            "Flight Number": booking_record.get("flight_number", "N/A"),
            "Route": (
                f"{booking_record.get('departure', 'N/A')} → "
                f"{booking_record.get('destination', 'N/A')}"
            ),
            "Date": booking_record.get("date", "N/A"),
            "Seat Class": booking_record.get("seat_class", "N/A"),
            "Total Fare": f"${booking_record.get('total_fare', 0):.2f}"
        }

        return formatted
