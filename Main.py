# FastAPI entry point for Jetstream Sprint 1.
# Exposes a /search endpoint using the search service.

from fastapi import FastAPI
from app.search_service import search_flights
from fastapi import FastAPI
from flight_search_api import flight_search_router

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
    
    # Mount the flight search API
app.include_router(flight_search_router, prefix="/api")
