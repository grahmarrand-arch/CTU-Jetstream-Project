from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from flight_search_ui import FlightSearchUI
from no_flights_ui import NoFlightsUI
from login_ui import LoginUI
from passenger_details_ui import PassengerDetailsUI
from search_service import search_flights
from password_utils import verify_password, hash_password

app = FastAPI()

search_ui = FlightSearchUI()
no_flights_ui = NoFlightsUI()
login_ui = LoginUI()
passenger_ui = PassengerDetailsUI()


@app.get("/", response_class=HTMLResponse)
def home():
    return HTMLResponse(content=search_ui.build_search_page(results=None))


@app.get("/search", response_class=HTMLResponse)
def search(departure: str = None, destination: str = None, date: str = None):
    if not departure or not destination or not date:
        return HTMLResponse(content=search_ui.build_search_page(results=None))

    results = search_flights(departure, destination, date)

    if not results:
        return HTMLResponse(content=no_flights_ui.build_page())

    return HTMLResponse(content=search_ui.build_search_page(results=results))


@app.get("/login", response_class=HTMLResponse)
def login_page():
    return HTMLResponse(content=login_ui.build_page())


@app.post("/login", response_class=HTMLResponse)
async def login(email: str = Form(...), password: str = Form(...)):
    stored_hash = hash_password("example123")
    if verify_password(password, stored_hash):
        return HTMLResponse(content=passenger_ui.build_page())
    return HTMLResponse(content=login_ui.build_invalid())


@app.get("/passenger", response_class=HTMLResponse)
def passenger_page():
    return HTMLResponse(content=passenger_ui.build_page())


@app.post("/submit_passenger", response_class=HTMLResponse)
async def submit_passenger(
    full_name: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    passport: str = Form(...),
    nationality: str = Form(...),
    seat_class: str = Form(...)
):
    lines = []
    lines.append("<html><body>")
    lines.append("<h2>Passenger Saved</h2>")
    lines.append("<p>Your details have been recorded.</p>")
    lines.append('<a href="/">Return Home</a>')
    lines.append("</body></html>")
    return HTMLResponse(content="\n".join(lines))
