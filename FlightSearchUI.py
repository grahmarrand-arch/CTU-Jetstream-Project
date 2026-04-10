# flight_search_ui.py
# Render-safe, GitHub-safe, standalone flight search UI generator for Jetstream LLC.
# Framework-agnostic: can be used with FastAPI, Flask, Django, or any custom Python backend.

from typing import List, Dict


class FlightSearchUI:
    # Generates HTML for the Jetstream flight search page and optional results table.

    def build_search_page(self, results: List[Dict] | None = None) -> str:
        # Main entry: returns a full HTML page as a string.
        # If results is provided, they will be rendered in a table below the form.

        head_lines = []
        head_lines.append("<!DOCTYPE html>")
        head_lines.append('<html lang="en">')
        head_lines.append("<head>")
        head_lines.append('    <meta charset="UTF-8">')
        head_lines.append("    <title>Jetstream Flight Search</title>")
        head_lines.append("    <style>")
        head_lines.append("        body {")
        head_lines.append("            font-family: Arial, sans-serif;")
        head_lines.append("            background: #eef4ff;")
        head_lines.append("            margin: 0;")
        head_lines.append("            padding: 0;")
        head_lines.append("            display: flex;")
        head_lines.append("            justify-content: center;")
        head_lines.append("            padding-top: 40px;")
        head_lines.append("        }")
        head_lines.append("        .search-container {")
        head_lines.append("            background: white;")
        head_lines.append("            padding: 25px;")
        head_lines.append("            width: 520px;")
        head_lines.append("            border-radius: 10px;")
        head_lines.append("            box-shadow: 0 0 12px rgba(0,0,0,0.15);")
        head_lines.append("        }")
        head_lines.append("        h2 {")
        head_lines.append("            text-align: center;")
        head_lines.append("            color: #003366;")
        head_lines.append("            margin-top: 0;")
        head_lines.append("        }")
        head_lines.append("        form {")
        head_lines.append("            display: grid;")
        head_lines.append("            grid-template-columns: 1fr 1fr;")
        head_lines.append("            gap: 12px;")
        head_lines.append("            margin-top: 15px;")
        head_lines.append("        }")
        head_lines.append("        .full-width {")
        head_lines.append("            grid-column: 1 / 3;")
        head_lines.append("        }")
        head_lines.append("        input, select {")
        head_lines.append("            width: 100%;")
        head_lines.append("            padding: 10px;")
        head_lines.append("            border-radius: 6px;")
        head_lines.append("            border: 1px solid #ccc;")
        head_lines.append("            font-size: 14px;")
        head_lines.append("        }")
        head_lines.append("        button {")
        head_lines.append("            width: 100%;")
        head_lines.append("            padding: 12px;")
        head_lines.append("            background: #003366;")
        head_lines.append("            color: white;")
        head_lines.append("            border: none;")
        head_lines.append("            border-radius: 6px;")
        head_lines.append("            cursor: pointer;")
        head_lines.append("            font-size: 15px;")
        head_lines.append("        }")
        head_lines.append("        button:hover {")
        head_lines.append("            background: #0055aa;")
        head_lines.append("        }")
        head_lines.append("        .results {")
        head_lines.append("            margin-top: 25px;")
        head_lines.append("        }")
        head_lines.append("        table {")
        head_lines.append("            width: 100%;")
        head_lines.append("            border-collapse: collapse;")
        head_lines.append("            font-size: 14px;")
        head_lines.append("        }")
        head_lines.append("        th, td {")
        head_lines.append("            border: 1px solid #ddd;")
        head_lines.append("            padding: 8px;")
        head_lines.append("            text-align: left;")
        head_lines.append("        }")
        head_lines.append("        th {")
        head_lines.append("            background: #003366;")
        head_lines.append("            color: white;")
        head_lines.append("        }")
        head_lines.append("        .no-results {")
        head_lines.append("            margin-top: 15px;")
        head_lines.append("            color: #555;")
        head_lines.append("            font-style: italic;")
        head_lines.append("        }")
        head_lines.append("    </style>")
        head_lines.append("</head>")
        head_lines.append("<body>")

        body_lines = []
        body_lines.append('    <div class="search-container">')
        body_lines.append("        <h2>Jetstream Flight Search</h2>")
        body_lines.append('        <form action="/search" method="GET">')
        body_lines.append('            <div>')
        body_lines.append('                <input type="text" name="departure" placeholder="Departure (e.g., JFK)" required>')
        body_lines.append("            </div>")
        body_lines.append('            <div>')
        body_lines.append('                <input type="text" name="destination" placeholder="Destination (e.g., LAX)" required>')
        body_lines.append("            </div>")
        body_lines.append('            <div class="full-width">')
        body_lines.append('                <input type="date" name="date" required>')
        body_lines.append("            </div>")
        body_lines.append('            <div class="full-width">')
        body_lines.append("                <button type=\"submit\">Search Flights</button>")
        body_lines.append("            </div>")
        body_lines.append("        </form>")

        if results is not None:
            body_lines.extend(self._build_results_section(results))

        body_lines.append("    </div>")
        body_lines.append("</body>")
        body_lines.append("</html>")

        html = "\n".join(head_lines + body_lines)
        return html

    def _build_results_section(self, results: List[Dict]) -> List[str]:
        # Builds the results section HTML as a list of lines.

        lines = []
        lines.append('        <div class="results">')
        if not results:
            lines.append('            <div class="no-results">No flights found for the selected criteria.</div>')
            lines.append("        </div>")
            return lines

        lines.append("            <table>")
        lines.append("                <thead>")
        lines.append("                    <tr>")
        lines.append("                        <th>Flight</th>")
        lines.append("                        <th>Route</th>")
        lines.append("                        <th>Date</th>")
        lines.append("                        <th>Departure Time</th>")
        lines.append("                        <th>Arrival Time</th>")
        lines.append("                        <th>Price (USD)</th>")
        lines.append("                    </tr>")
        lines.append("                </thead>")
        lines.append("                <tbody>")

        for flight in results:
            flight_number = flight.get("flight_number", "N/A")
            departure = flight.get("departure", "N/A")
            destination = flight.get("destination", "N/A")
            date = flight.get("date", "N/A")
            departure_time = flight.get("departure_time", "N/A")
            arrival_time = flight.get("arrival_time", "N/A")
            price = flight.get("price", "N/A")

            lines.append("                    <tr>")
            lines.append(f"                        <td>{flight_number}</td>")
            lines.append(f"                        <td>{departure} → {destination}</td>")
            lines.append(f"                        <td>{date}</td>")
            lines.append(f"                        <td>{departure_time}</td>")
            lines.append(f"                        <td>{arrival_time}</td>")
            lines.append(f"                        <td>{price}</td>")
            lines.append("                    </tr>")

        lines.append("                </tbody>")
        lines.append("            </table>")
        lines.append("        </div>")
        return lines


# Example integration snippet (for FastAPI):
#
# from fastapi import FastAPI, Request
# from fastapi.responses import HTMLResponse
# from flight_search_ui import FlightSearchUI
#
# app = FastAPI()
# ui = FlightSearchUI()
#
# @app.get("/search", response_class=HTMLResponse)
# async def search_flights(request: Request, departure: str | None = None,
#                          destination: str | None = None, date: str | None = None):
#     if not departure or not destination or not date:
#         html = ui.build_search_page(results=None)
#         return HTMLResponse(content=html)
#
#     # Replace this with real DB search logic.
#     mock_results = [
#         {
#             "flight_number": "JS101",
#             "departure": departure,
#             "destination": destination,
#             "date": date,
#             "departure_time": "08:00",
#             "arrival_time": "11:15",
#             "price": "$320.00"
#         }
#     ]
#     html = ui.build_search_page(results=mock_results)
#     return HTMLResponse(content=html)
