# Jetstream LLC — Sprint 1
## Flight Search Module (Departure, Destination, Date)

Jetstream LLC is developing a modern airline web application.  
Sprint 1 focuses on implementing the foundational Flight Search feature.

---

## Sprint 1 Deliverables
✔ MySQL flights table  
✔ Python database connection  
✔ Search filters (departure, destination, date)  
✔ Display results with price + times  
✔ Optional FastAPI endpoint  
✔ Fully commented code  
✔ Agile sprint hour breakdown  

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

---

## Sprint 1 Work Hours (Agile Estimate)

| Task | Hours |
|------|-------|
| Create MySQL Schema | 2 |
| Build DB Connection | 1 |
| Implement Search Logic | 3 |
| Test Search Function | 2 |
| Display Formatting | 1 |
| FastAPI Endpoint | 2 |
| Documentation + Comments | 2 |

**Total: 13 hours**

---

## End of Sprint 1
This module is now ready for integration into the Jetstream backend.
jetstream-backend/README.md