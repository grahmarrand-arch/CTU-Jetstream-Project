# Handles all Sprint 1 flight search logic.
# Filters by departure, destination, and date.
# Returns price and flight times for display.

from app.database import get_connection

def search_flights(departure=None, destination=None, date=None):
    # Searches flights using Sprint 1 filters:
    # - departure
    # - destination
    # - date (YYYY-MM-DD)
    #
    # Returns a list of matching flights with:
    # - flight number
    # - departure/arrival times
    # - price

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Base SQL query selecting required fields.
    # Render-safe: no triple-quoted SQL blocks.
    query = (
        "SELECT "
        "id, "
        "flight_number, "
        "departure, "
        "destination, "
        "departure_datetime, "
        "arrival_datetime, "
        "price "
        "FROM flights "
        "WHERE 1=1"
    )

    params = []

    # Filter by departure airport/city
    if departure:
        query += " AND departure = %s"
        params.append(departure)

    # Filter by destination airport/city
    if destination:
        query += " AND destination = %s"
        params.append(destination)

    # Filter by date (ignores time)
    if date:
        query += " AND DATE(departure_datetime) = %s"
        params.append(date)

    cursor.execute(query, params)
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return results
