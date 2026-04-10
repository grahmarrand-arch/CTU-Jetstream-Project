# Jetstream LLC – Sprint 1  
## Flight Search and User System Modules

Jetstream LLC is developing a modern airline web application.  
Sprint 1 focuses on implementing the foundational Flight Search feature and core user system components.

## Sprint 1 Deliverables
- MySQL flights table  
- Python database connection  
- Search filters (departure, destination, date)  
- User registration and login modules  
- Password hashing and verification  
- Payment and card validation modules  
- Dashboard booking formatter  
- Confirmation email generator  
- CI/CD pipeline  
- HTML UI pages  
- Fully commented, Render-safe code  
- Agile sprint hour breakdown  

## Project Structure

jetstream-backend  
│  
├── app  
│   ├── database.py  
│   ├── search_service.py  
│   ├── registration_service.py  
│   ├── login_controller.py  
│   ├── confirmation_email_template.py  
│   ├── dashboard_booking_display.py  
│   ├── payment_handler.py  
│   ├── card_validator.py  
│   ├── fare_calculator.py  
│   ├── password_utils.py  
│   ├── main.py  
│   └── __init__.py  
│  
├── html  
│   ├── login.html  
│   └── passenger_details.html  
│  
├── sql  
│   └── flights.sql  
│  
├── utils  
│   └── project_architecture.py  
│  
├── cicd  
│   └── ci_cd_pipeline.py  
│  
├── README.md  
└── requirements.txt  

## How to Run

1. Install dependencies:  
   `pip install -r requirements.txt`

2. Start the FastAPI server:  
   `uvicorn app.main:app --reload`

3. Test the search endpoint:  
   `http://localhost:8000/search?departure=JFK&destination=LAX&date=2026-05-10`

4. Open the login UI (if served statically):  
   `http://localhost:8000/login`

5. Submit passenger details (if connected to backend):  
   `http://localhost:8000/submit_passenger`
