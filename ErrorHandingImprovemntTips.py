# =========================
# Custom Exception Class
# =========================

class AppError(Exception):
    def __init__(self, message, status_code=400):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


# =========================
# Standard API Response Helpers
# =========================

def success_response(message, data=None):
    return {
        "success": True,
        "message": message,
        "data": data or {}
    }, 200


def error_response(message, code=400):
    return {
        "success": False,
        "error": {
            "message": message,
            "code": code
        }
    }, code


# =========================
# Global Error Handler Decorator
# =========================

def handle_errors(func):
    """
    Wraps functions to ensure consistent error handling
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except AppError as e:
            return error_response(e.message, e.status_code)

        except ValueError:
            return error_response(
                "Invalid input provided. Please check your data and try again.",
                400
            )

        except Exception:
            return error_response(
                "Unexpected system error. Please try again later.",
                500
            )

    return wrapper


# =========================
# Mock Data (Airline System)
# =========================

FLIGHTS = {
    101: {"from": "NYC", "to": "LA", "price": 250},
    202: {"from": "LA", "to": "SF", "price": 120}
}

AVAILABLE_SEATS = {
    101: ["1A", "1B", "2A"],
    202: ["1A", "2B"]
}


# =========================
# Business Logic Functions
# =========================

@handle_errors
def search_flight(flight_id):
    if flight_id not in FLIGHTS:
        raise AppError("No flights found for the selected route.", 404)

    return success_response(
        "Flight found successfully",
        FLIGHTS[flight_id]
    )


@handle_errors
def book_flight(user_id, flight_id):
    if not user_id:
        raise AppError("Session expired. Please log in again.", 401)

    if flight_id not in FLIGHTS:
        raise AppError("Selected flight does not exist.", 404)

    return success_response("Flight booked successfully!")


@handle_errors
def select_seat(flight_id, seat):
    if flight_id not in AVAILABLE_SEATS:
        raise AppError("Flight seating data not available.", 404)

    if seat not in AVAILABLE_SEATS[flight_id]:
        return error_response(
            "This seat is unavailable. Please choose another seat.",
            409
        )

    # simulate seat reservation
    AVAILABLE_SEATS[flight_id].remove(seat)

    return success_response(f"Seat {seat} reserved successfully.")


# =========================
# Example Usage
# =========================

if __name__ == "__main__":
    print(search_flight(101))
    print(book_flight(1, 999))       # triggers user-friendly error
    print(select_seat(101, "1A"))    # success
    print(select_seat(101, "9Z"))    # seat error