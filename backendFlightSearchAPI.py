# flight_search_api.py
# Jetstream LLC - Standalone Backend Flight Search API Module
# -----------------------------------------------------------
# This module provides a fully functional backend API for searching flights.
# It is designed to be imported into a main FastAPI application or run independently.
# All code is Render-safe, GitHub-friendly, and free of JSON/YAML-breaking syntax.

import mysql.connector
from fastapi import APIRouter, HTTPException
from fastapi import Query

# -----------------------------------------------------------
# Flight Search Router
# -----------------------------------------------------------
# This router can be mounted inside main.py using:
# app.include_router(flight_search_router, prefix="/api")
flight_search_router = APIRouter()


# -----------------------------------------------------------
# Database Connection Helper
# -----------------------------------------------------------
# Creates a new MySQL connection each time the API is called.
# This avoids connection pooling issues on Render.
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",          # Replace with Render MySQL host
            user="root",               # Replace with your DB username
            password="password123",    # Replace with your DB password
            database="jetstream_db"    # Replace with your DB name
        )
        return connection
    except mysql.connector.Error as error:
        raise HTTPException(status_code=500, detail="Database connection failed")


# -----------------------------------------------------------
# Flight Search API Endpoint
# -----------------------------------------------------------
# Example request:
# /api/search-flights?departure=JFK&destination=LAX&date=2026-05-10
@flight_search_router.get("/search-flights")
def search_flights(
    departure: str = Query(..., description="Departure airport code"),
    destination: str = Query(..., description="Destination airport code"),
    date: str = Query(..., description="Flight departure date in YYYY-MM-DD format")
):
    # Connect to MySQL
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    # SQL query to filter flights by departure, destination, and date
    query = (
        "SELECT flight_id, airline, departure, destination, departure_time, "
        "arrival_time, price FROM flights "
        "WHERE departure = %s AND destination = %s AND DATE(departure_time) = %s"
    )

    # Execute query with user-provided parameters
    cursor.execute(query, (departure, destination, date))
    results = cursor.fetchall()

    # Close DB connection
    cursor.close()
    db.close()

    # If no flights found, return a friendly message
    if not results:
        return {
            "status": "no_results",
            "message": "No flights found for the selected route and date",
            "flights": []
        }

    # Return successful search results
    return {
        "status": "success",
        "total_results": len(results),
        "flights": results
    }
