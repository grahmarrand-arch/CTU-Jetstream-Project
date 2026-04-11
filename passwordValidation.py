# password_rules.py
# Jetstream LLC - Strong Password Validation Module
# -----------------------------------------------------------
# This module validates password strength using simple Python logic.
# It is fully standalone and can be imported into any backend service.

import re

def is_strong_password(password):
    # Enforce minimum length
    if len(password) < 8:
        return False

    # Require uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Require lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Require digit
    if not re.search(r"[0-9]", password):
        return False

    # Require special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True
