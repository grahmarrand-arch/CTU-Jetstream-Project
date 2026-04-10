Jetstream LLC - Sprint 1 Backend Overview

This project contains the backend modules for Jetstream Airline.
All files are written in a Render-safe format to avoid YAML or JSON parsing issues.

Included Modules:
- Database.py
- SearchService.py
- RegistrationLogic.py
- LoginController.py
- ConfirmationEmailTemplate.py
- DisplayBookingDashboard.py
- PasswordDetails.py
- PaymentSuccessFailureHandler.py
- PasswordHash.py
- TotalFareCal.py
- Main.py

Included HTML Files:
- LoginUI.html
- PassengerDetails.html

Included SQL Files:
- FlightsFilters.sql

Included CI/CD Tools:
- CICDPipline.py

How to Run:
Install dependencies using:
pip install -r requirements.txt

Start the FastAPI server:
uvicorn app.main:app --reload

Test the search endpoint:
http://localhost:8000/search?departure=JFK&destination=LAX&date=2026-05-10
