from flask import Flask, render_template_string, request

app = Flask(__name__)

# Sample booking data
BOOKINGS = [
    {
        "id": "BK001",
        "airline": "Delta",
        "flight_number": "DL101",
        "departure": "JFK",
        "destination": "LAX",
        "date": "2026-04-10",
        "time": "10:00 AM",
        "status": "Confirmed",
        "price": 320
    },
    {
        "id": "BK002",
        "airline": "United",
        "flight_number": "UA202",
        "departure": "ORD",
        "destination": "MIA",
        "date": "2026-04-08",
        "time": "02:00 PM",
        "status": "Cancelled",
        "price": 210
    },
    {
        "id": "BK003",
        "airline": "American Airlines",
        "flight_number": "AA330",
        "departure": "DFW",
        "destination": "SFO",
        "date": "2026-04-12",
        "time": "06:30 AM",
        "status": "Pending",
        "price": 280
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Booking History Dashboard</title>
    <style>
        body {
            font-family: Arial;
            background: #f4f6f9;
            margin: 0;
        }

        .container {
            width: 90%;
            margin: auto;
        }

        .header {
            padding: 20px;
            font-size: 26px;
            font-weight: bold;
        }

        .filters {
            margin-bottom: 20px;
            display: flex;
            gap: 10px;
        }

        input, select {
            padding: 8px;
            border-radius: 6px;
            border: 1px solid #ccc;
        }

        .card {
            background: white;
            padding: 15px;
            margin-bottom: 12px;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }

        .top-row {
            display: flex;
            justify-content: space-between;
        }

        .status {
            padding: 4px 10px;
            border-radius: 5px;
            color: white;
            font-size: 12px;
        }

        .confirmed { background: green; }
        .cancelled { background: red; }
        .pending { background: orange; }

        .actions button {
            padding: 6px 10px;
            margin-right: 5px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .view { background: #3498db; color: white; }
        .cancel { background: #e74c3c; color: white; }
    </style>
</head>
<body>

<div class="container">

    <div class="header">✈ Booking History Dashboard</div>

    <form class="filters" method="get">
        <input type="text" name="search" placeholder="Search booking ID or flight...">
        <select name="status">
            <option value="">All Status</option>
            <option value="Confirmed">Confirmed</option>
            <option value="Cancelled">Cancelled</option>
            <option value="Pending">Pending</option>
        </select>
        <button type="submit">Filter</button>
    </form>

    {% for b in bookings %}
    <div class="card">
        <div class="top-row">
            <div>
                <strong>{{ b.airline }} {{ b.flight_number }}</strong><br>
                {{ b.departure }} → {{ b.destination }}<br>
                {{ b.date }} | {{ b.time }}
            </div>

            <div>
                <span class="status {{ b.status|lower }}">
                    {{ b.status }}
                </span>
            </div>
        </div>

        <hr>

        <div class="top-row">
            <div><strong>${{ b.price }}</strong></div>

            <div class="actions">
                <button class="view">View</button>
                {% if b.status == "Confirmed" %}
                <button class="cancel">Cancel</button>
                {% endif %}
            </div>
        </div>
    </div>
    {% endfor %}

</div>

</body>
</html>
"""

@app.route("/", methods=["GET"])
def dashboard():
    search = request.args.get("search", "").lower()
    status = request.args.get("status", "")

    filtered = BOOKINGS

    # Filter by search
    if search:
        filtered = [
            b for b in filtered
            if search in b["id"].lower()
            or search in b["flight_number"].lower()
            or search in b["airline"].lower()
        ]

    # Filter by status
    if status:
        filtered = [b for b in filtered if b["status"] == status]

    return render_template_string(HTML_TEMPLATE, bookings=filtered)

if __name__ == "__main__":
    app.run(debug=True)