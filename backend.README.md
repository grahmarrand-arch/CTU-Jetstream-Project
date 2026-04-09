# Jetstream LLC, Sprint 1
## Flight Search Module (Departure, Destination, Date)

Jetstream LLC is developing a modern airline web application.  
Sprint 1 focuses on implementing the foundational Flight Search feature.

---

## Sprint 1 Deliverables
- MySQL flights table  
- Python database connection  
- Search filters (departure, destination, date)  
- Display results with price + times  
- Optional FastAPI endpoint  
- Fully commented code  
- Agile sprint hour breakdown 

---

## Project Structure

jetstream-backend/
│
├── app/
│   ├── database.py
│   ├── search_service.py
│   ├── main.py
│   └── __init__.py
│
├── sql/
│   └── flights.sql
│
├── README.md
└── requirements.txt

---

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run FastAPI server:
   uvicorn app.main:app --reload

3. Test search endpoint:
   http://localhost:8000/search?departure=JFK&destination=LAX&date=2026-05-10

