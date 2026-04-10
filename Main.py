# FastAPI entry point for Jetstream Sprint 1.
# Exposes a /search endpoint using the search service.
# Triple-quoted strings were removed to avoid Render JSON parsing issues.

from fastapi import FastAPI
from app.search_service import search_flights
from fastapi.responses import HTMLResponse
from no_flights_ui import NoFlightsUI

app = FastAPI()
ui = NoFlightsUI()

@app.get("/no-flights", response_class=HTMLResponse)
def no_flights():
    return ui.build_page()

# Create the FastAPI application instance
app = FastAPI()

@app.get("/search")
def search(departure: str = None, destination: str = None, date: str = None):
    """
    Example usage:
        /search?departure=JFK&destination=LAX&date=2026-05-10

    This endpoint calls the search_flights service and returns
    a list of matching flights in JSON format.
    """
    return {"flights": search_flights(departure, destination, date)}
