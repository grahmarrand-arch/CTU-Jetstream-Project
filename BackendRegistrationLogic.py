"""
This module handles all backend user registration logic.
It is intentionally designed as a standalone component so it can be
plugged into any Python-based backend (FastAPI, Flask, custom framework, etc.).

Dependencies:
- password_utils.py for hashing
- confirmation_messages.py for standardized responses
"""

from password_utils import hash_password
from confirmation_messages import success_message, error_message


class RegistrationService:
    """
    RegistrationService encapsulates all logic related to creating new users.
    The database layer is passed in at runtime to keep this module decoupled.
    """

    def __init__(self, db):
        """
        Constructor receives a database interface object.
        The 'db' object must expose:
            - get_user_by_email(email)
            - create_user(username, email, hashed_password)
        """
        self.db = db

    def register_user(self, username: str, email: str, password: str):
        """
        Main registration function.

        Steps performed:
        1. Validate input fields
        2. Check if user already exists
        3. Hash password securely
        4. Insert new user into database
        5. Return a standardized confirmation message
        """

        # --- Step 1: Validate input ---
        if not username or not email or not password:
            # Missing fields → return error response
            return error_message("All fields are required.")

        # --- Step 2: Check if user already exists ---
        existing_user = self.db.get_user_by_email(email)
        if existing_user:
            # Email already in use → return error response
            return error_message("Email already registered.")

        # --- Step 3: Hash the password using bcrypt ---
        hashed_pw = hash_password(password)

        # --- Step 4: Insert user into database ---
        try:
            # Attempt to create the user record
            self.db.create_user(username, email, hashed_pw)
        except Exception as e:
            # Any database failure is caught and returned as an error message
            return error_message(f"Database error: {str(e)}")

        # --- Step 5: Return success message ---
        return success_message("Registration successful! Welcome to Jetstream.")
