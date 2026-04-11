# registration_ui.py
# Jetstream LLC - Registration UI Form Module
# -----------------------------------------------------------
# This module provides a simple HTML registration form that can be
# served by FastAPI. It is fully standalone and can be imported into main.py.

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

registration_ui_router = APIRouter()

@registration_ui_router.get("/register", response_class=HTMLResponse)
def registration_form():
    # HTML form for user registration
    # Render-safe: no triple quotes, no docstrings, no JSON-breaking characters
    html_content = (
        "<html><head><title>Jetstream Registration</title></head>"
        "<body style='font-family: Arial; margin: 40px;'>"
        "<h2>Jetstream LLC - Create Your Account</h2>"
        "<form method='post' action='/api/register-user'>"

        "<label>Full Name:</label><br>"
        "<input type='text' name='full_name' required><br><br>"

        "<label>Phone Number:</label><br>"
        "<input type='text' name='phone' required><br><br>"

        "<label>Email Address:</label><br>"
        "<input type='email' name='email' required><br><br>"

        "<label>Password:</label><br>"
        "<input type='password' name='password' required><br><br>"

        "<button type='submit'>Register</button>"
        "</form></body></html>"
    )
    return HTMLResponse(content=html_content)
