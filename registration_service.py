# registration_service.py
# Jetstream LLC - Secure User Registration Backend Module
# -----------------------------------------------------------
# This module handles:
# - Validating form input
# - Checking for existing users
# - Hashing passwords with bcrypt
# - Storing user data in MySQL
# - Returning safe JSON responses
# All code is Render-safe and GitHub-friendly.

import mysql.connector
from fastapi import APIRouter, Form, HTTPException
import bcrypt
from password_rules import is_strong_password

registration_service_router = APIRouter()


# -----------------------------------------------------------
# Database Connection Helper
# -----------------------------------------------------------
# Creates a new MySQL connection for each request.
# Uses specific exception handling to avoid linter error E772.
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",          # Replace with Render MySQL host
            user="root",               # Replace with your DB username
            password="password123",    # Replace with your DB password
            database="jetstream_db"    # Replace with your DB name
        )
        return connection

    except mysql.connector.Error as db_error:
        # Return a clean FastAPI error instead of crashing
        raise HTTPException(
            status_code=500,
            detail="Database connection failed: " + str(db_error)
        )


# -----------------------------------------------------------
# Registration Endpoint
# -----------------------------------------------------------
# Accepts form data from the registration UI and stores the user securely.
@registration_service_router.post("/register-user")
def register_user(
    full_name: str = Form(...),
    phone: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    # Validate password strength
    if not is_strong_password(password):
        raise HTTPException(
            status_code=400,
            detail="Password is too weak. Must include uppercase, lowercase, digit, special character, and be at least 8 characters long."
        )

    # Connect to database
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    # Check if email already exists
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    existing_user = cursor.fetchone()

    if existing_user:
        cursor.close()
        db.close()
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash password securely using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    # Insert new user into database
    insert_query = (
        "INSERT INTO users (full_name, phone, email, password_hash) "
        "VALUES (%s, %s, %s, %s)"
    )

    try:
        cursor.execute(insert_query, (full_name, phone, email, hashed_password))
        db.commit()

    except mysql.connector.Error as insert_error:
        cursor.close()
        db.close()
        raise HTTPException(
            status_code=500,
            detail="Database insert failed: " + str(insert_error)
        )

    # Close DB connection
    cursor.close()
    db.close()

    # Return success response
    return {
        "status": "success",
        "message": "User registered successfully"
    }
