from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS (important for dashboard API calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Fake in-memory database
# -------------------------
bookings = [
    {"id": 1, "flight": "NYC → LAX", "date": "2026-05-01", "status": "Confirmed"},
    {"id": 2, "flight": "LAX → SFO", "date": "2026-05-03", "status": "Confirmed"},
    {"id": 3, "flight": "MIA → ORD", "date": "2026-05-05", "status": "Confirmed"},
]

# -------------------------
# API ROUTES
# -------------------------
@app.get("/api/bookings")
def get_bookings():
    return bookings


@app.delete("/api/bookings/{booking_id}")
def cancel_booking(booking_id: int):
    global bookings
    bookings = [
        b for b in bookings
        if b["id"] != booking_id
    ]
    return {"message": f"Booking {booking_id} cancelled"}


# -------------------------
# DASHBOARD UI (FRONTEND)
# -------------------------
@app.get("/", response_class=HTMLResponse)
def dashboard():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>Booking Dashboard</title>
    <style>
        body { font-family: Arial; margin: 30px; background: #f4f4f4; }
        .card { background: white; padding: 15px; margin: 10px 0; border-radius: 8px; }
        button { background: red; color: white; border: none; padding: 6px 10px; cursor: pointer; }
    </style>
</head>
<body>

<h1>✈️ Booking Dashboard</h1>
<div id="bookings"></div>

<script>
async function loadBookings() {
    const res = await fetch("/api/bookings");
    const data = await res.json();

    const container = document.getElementById("bookings");
    container.innerHTML = "";

    data.forEach(b => {
        const div = document.createElement("div");
        div.className = "card";

        div.innerHTML = `
            <h3>${b.flight}</h3>
            <p>Date: ${b.date}</p>
            <p>Status: ${b.status}</p>
            <button onclick="cancelBooking(${b.id})">Cancel Booking</button>
        `;

        container.appendChild(div);
    });
}

async function cancelBooking(id) {
    await fetch(`/api/bookings/${id}`, { method: "DELETE" });
    loadBookings();
}

loadBookings();
</script>

</body>
</html>
"""

# -------------------------
# RUN:
# uvicorn main:app --reload
# -------------------------