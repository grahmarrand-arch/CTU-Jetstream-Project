from flask import Flask, request, redirect, url_for, render_template_string, flash

app = Flask(__name__)
app.secret_key = "secret"

# -----------------------
# Fake in-memory database
# -----------------------
BOOKINGS = [
    {"id": 1, "flight": "AA101", "seat": "12A", "status": "Confirmed"},
    {"id": 2, "flight": "DL202", "seat": "7C", "status": "Confirmed"},
    {"id": 3, "flight": "UA303", "seat": "9B", "status": "Confirmed"},
]


# -----------------------
# Helper functions
# -----------------------
def get_booking(booking_id):
    return next((b for b in BOOKINGS if b["id"] == booking_id), None)


# -----------------------
# Routes
# -----------------------
@app.route("/")
def dashboard():
    html = """
    <h1>My Dashboard</h1>

    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul style="color: green;">
          {% for msg in messages %}
            <li>{{ msg }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}

    <h2>My Bookings</h2>

    {% for b in bookings %}
      <div style="border:1px solid #ccc; padding:10px; margin:10px;">
        <p><b>Flight:</b> {{ b.flight }}</p>
        <p><b>Seat:</b> {{ b.seat }}</p>
        <p><b>Status:</b> {{ b.status }}</p>

        {% if b.status != "Cancelled" %}
          <form method="POST" action="/cancel/{{ b.id }}">
            <button type="submit"
              onclick="return confirm('Are you sure you want to cancel this booking?')">
              Cancel Booking
            </button>
          </form>
        {% else %}
          <span style="color:red;">Cancelled</span>
        {% endif %}
      </div>
    {% endfor %}
    """
    return render_template_string(html, bookings=BOOKINGS)


@app.route("/cancel/<int:booking_id>", methods=["POST"])
def cancel_booking(booking_id):
    booking = get_booking(booking_id)

    if not booking:
        flash("Booking not found")
        return redirect(url_for("dashboard"))

    if booking["status"] == "Cancelled":
        flash("Booking already cancelled")
        return redirect(url_for("dashboard"))

    # Cancel booking
    booking["status"] = "Cancelled"

    flash(f"Booking {booking_id} cancelled successfully")
    return redirect(url_for("dashboard"))


# -----------------------
# Run app
# -----------------------
if __name__ == "__main__":
    app.run(debug=True)