Jetstream LLC - Flight Search and Booking Platform

This project contains the backend and frontend components for Jetstream LLC.
All files are written in a Render-safe format to avoid YAML or JSON parsing issues.
The application is built using FastAPI, MySQL, SQLAlchemy, and Jinja2 templates.

Project Summary
The system provides a flight search interface, backend API, database integration, and HTML templates for user interaction. Future iterations will include registration, login, booking, payment, and dashboard modules.

Included Python Modules
main.py
config.py
db.py
models.py
schemas.py
crud.py

Included HTML Templates
templates_base.html
templates_search.html
templates_results.html

Included SQL Files
schema.sql

Included Test Files
tests/test_search.py

Included Requirements File
requirements.txt

How to Run Locally
Install dependencies using the command
pip install -r requirements.txt

Set the database URL environment variable
DATABASE_URL must point to a valid MySQL database

Start the FastAPI server
uvicorn main:app --host 0.0.0.0 --port 8000

Access the application in a browser
http://localhost:8000

Flight Search Endpoint
http://localhost:8000/api/flights

Render Deployment Notes
Render must have the DATABASE_URL environment variable set
Render automatically detects Python projects
No JSON or YAML configuration files are required
README is plain text to prevent Render from misinterpreting it as a config file

Project Goals
Create a scalable airline booking system
Ensure all modules are GitHub friendly
Ensure all modules are Render safe
Support future expansion including registration, login, booking, payment, and dashboard features
