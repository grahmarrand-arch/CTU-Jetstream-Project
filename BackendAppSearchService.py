"""
search_service.py
Handles all Sprint 1 flight search logic.
Filters by departure, destination, and date.
Returns price and flight times for display.
"""

from app.database import get_connection

def search_flights(departure=None, destination=None, date=None):
    """
    Searches flights using Sprint 1 filters:
    - departure
    - destination
    - date (YYYY-MM-DD)

    Returns:
        List of matching flights with:
        - flight number
        - departure/arrival times
        - price
    """

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)  # Return rows as dicts

    # Base query selecting all required fields
    query = """
        SELECT
            id,
            flight_number,
            departure,
            destination,
            departure_datetime,
            arrival_datetime,
            price
        FROM flights
        WHERE 1=1
    """

    params = []

    # Filter: departure airport/city
    if departure:
        query += " AND departure = %s"
        params.append(departure)

    # Filter: destination airport/city
    if destination:
        query += " AND destination = %s"
        params.append(destination)

    # Filter: date only (ignore time)
    if date:
        query += " AND DATE(departure_datetime) = %s"
        params.append(date)

    cursor.execute(query, params)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results
