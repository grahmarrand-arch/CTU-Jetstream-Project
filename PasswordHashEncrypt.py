# Handles password hashing and verification for Jetstream.
# Uses bcrypt, a secure industry-standard hashing algorithm.
# bcrypt automatically salts passwords and is slow by design,
# which helps protect against brute-force attacks.

import bcrypt


def hash_password(plain_password: str) -> str:
    # Hashes a plaintext password using bcrypt.
    #
    # Steps:
    # 1. Convert password to bytes
    # 2. Generate a random salt
    # 3. Hash the password + salt
    # 4. Return the hash as a UTF-8 string

    password_bytes = plain_password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Verifies a plaintext password against a stored bcrypt hash.
    # Returns True if the password matches, False otherwise.

    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )
