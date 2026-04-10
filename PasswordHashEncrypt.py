"""

This module handles password hashing and verification.
It uses bcrypt, which is a secure, industry-standard hashing algorithm.

Why bcrypt?
- It automatically salts passwords
- It is slow by design (protects against brute-force attacks)
- It is widely used in production systems
"""

import bcrypt


def hash_password(plain_password: str) -> str:
    """
    Hashes a plaintext password using bcrypt.

    Steps:
    1. Convert password to bytes
    2. Generate a random salt
    3. Hash the password + salt
    4. Return the hash as a UTF-8 string
    """
    # Convert password to bytes (bcrypt requires byte strings)
    password_bytes = plain_password.encode("utf-8")

    # Generate a secure salt
    salt = bcrypt.gensalt()

    # Hash the password using bcrypt
    hashed = bcrypt.hashpw(password_bytes, salt)

    # Convert hash back to string for database storage
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plaintext password against a stored bcrypt hash.

    Returns:
        True if the password matches the hash
        False otherwise
    """
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )
