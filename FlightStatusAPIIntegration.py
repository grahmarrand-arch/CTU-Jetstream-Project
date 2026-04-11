from fastapi import FastAPI, Query
import requests
import os
from typing import Optional

app = FastAPI(title="Flight Status API")

# =========================
# CONFIG
# =========================
AVIATIONSTACK_KEY = os.getenv("AVIATIONSTACK_KEY", "demo_key")
BASE_URL = "https://api.aviationstack.com/v1/flights"

# =========================
# CORE SERVICE
# =========================
def fetch_flight_data(flight_iata: Optional[str] = None,
                       dep_iata: Optional[str] = None,
                       arr_iata: Optional[str] = None):

    params = {
        "access_key": AVIATIONSTACK_KEY,
        "flight_iata": flight_iata,
        "dep_iata": dep_iata,
        "arr_iata": arr_iata
    }

    # remove empty params
    params = {k: v for k, v in params.items() if v}

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            "success": True,
            "source": "aviationstack",
            "count": len(data.get("data", [])),
            "flights": data.get("data", [])
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "Request timed out",
            "flights": []
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": str(e),
            "flights": []
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}",
            "flights": []
        }


# =========================
# API ENDPOINT
# =========================
@app.get("/flight-status")
def get_flight_status(
    flight_iata: Optional[str] = Query(None, description="Flight number e.g. AA100"),
    dep_iata: Optional[str] = Query(None, description="Departure airport code e.g. JFK"),
    arr_iata: Optional[str] = Query(None, description="Arrival airport code e.g. LAX")
):

    if not flight_iata and not dep_iata and not arr_iata:
        return {
            "success": False,
            "error": "Please provide at least one query: flight_iata, dep_iata, or arr_iata",
            "flights": []
        }

    result = fetch_flight_data(flight_iata, dep_iata, arr_iata)

    # Optional normalization (clean frontend-friendly output)
    if result["success"]:
        normalized = []
        for f in result["flights"]:
            flight = f.get("flight", {})
            departure = f.get("departure", {})
            arrival = f.get("arrival", {})
            live = f.get("live", {})

            normalized.append({
                "flight": flight.get("iata"),
                "airline": flight.get("iata"),
                "status": f.get("flight_status"),
                "departure_airport": departure.get("iata"),
                "arrival_airport": arrival.get("iata"),
                "scheduled_departure": departure.get("scheduled"),
                "estimated_arrival": arrival.get("estimated"),
                "live_position": {
                    "latitude": live.get("latitude"),
                    "longitude": live.get("longitude"),
                    "altitude": live.get("altitude"),
                    "speed": live.get("speed")
                } if live else None
            })

        result["flights"] = normalized

    return result


# =========================
# RUN (optional)
# =========================
# Run with:
# uvicorn filename:app --reload