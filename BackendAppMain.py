"""
FastAPI entry point for Jetstream Sprint 1.
Exposes a /search endpoint using the search service.
"""

from fastapi import FastAPI
from app.search_service import search_flights

app = FastAPI()

@app.get("/search")
def search(departure: str = None, destination: str = None, date: str = None):
    """
    Example:
        /search?departure=JFK&destination=LAX&date=2026-05-10
    """
    return {"flights": search_flights(departure, destination, date)}
