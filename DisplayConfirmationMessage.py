"""
confirmation_messages.py
------------------------
Provides standardized success and error message formats.
This keeps backend responses consistent across all Jetstream services.
"""


def success_message(message: str) -> dict:
    """
    Wraps a success message in a consistent JSON structure.

    Example output:
    {
        "status": "success",
        "message": "Registration complete!"
    }
    """
    return {
        "status": "success",
        "message": message
    }


def error_message(message: str) -> dict:
    """
    Wraps an error message in a consistent JSON structure.

    Example output:
    {
        "status": "error",
        "message": "Email already exists."
    }
    """
    return {
        "status": "error",
        "message": message
    }
