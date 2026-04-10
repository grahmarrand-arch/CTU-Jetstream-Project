# Handles login logic for Jetstream LLC.
# Responsibilities:
# - Validate login input
# - Retrieve user from database
# - Verify password using bcrypt
# - Return standardized success/error messages

from password_utils import verify_password
from confirmation_messages import success_message, error_message


class LoginController:
    # Encapsulates all logic related to user authentication.
    # The database interface is injected at runtime to keep this module decoupled.

    def __init__(self, db):
        # Constructor receives a database interface object.
        # The 'db' object must expose:
        # - get_user_by_email(email)
        self.db = db

    def login(self, email: str, password: str):
        # Attempts to log in a user.
        #
        # Steps:
        # 1. Validate input fields
        # 2. Retrieve user from database
        # 3. Verify password using bcrypt
        # 4. Return success or error message

        # Step 1: Validate input
        if not email or not password:
            return error_message("Email and password are required.")

        # Step 2: Retrieve user from database
        user = self.db.get_user_by_email(email)
        if not user:
            # Generic error for security best practices
            return error_message("Invalid email or password.")

        # Step 3: Verify password using bcrypt
        if not verify_password(password, user["password"]):
            return error_message("Invalid email or password.")

        # Step 4: Login successful
        return success_message("Login successful. Redirecting to dashboard...")
