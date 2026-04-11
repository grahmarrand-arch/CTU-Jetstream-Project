import streamlit as st
import time
import re

# Mock database (replace with real API later)
FLIGHT_DB = {
    "AA101": {
        "airline": "American Airlines",
        "status": "On Time",
        "departure": "JFK",
        "arrival": "LAX",
        "departure_time": "10:30 AM",
        "arrival_time": "1:45 PM",
    },
    "DL202": {
        "airline": "Delta Airlines",
        "status": "Delayed",
        "departure": "ATL",
        "arrival": "ORD",
        "departure_time": "2:00 PM",
        "arrival_time": "3:30 PM",
    }
}

# Page config
st.set_page_config(page_title="Flight Status Search", page_icon="✈️", layout="centered")

st.title("✈️ Flight Status Search")
st.write("Enter your flight number to check current status.")

# Input
flight_number = st.text_input("Flight Number (e.g. AA101)").upper().strip()

def is_valid_flight_number(fn):
    return re.match(r"^[A-Z]{2}\d{1,4}$", fn)

# Search button
if st.button("Check Status"):

    if not flight_number:
        st.error("Please enter a flight number.")
    elif not is_valid_flight_number(flight_number):
        st.warning("Invalid format. Use format like AA101.")
    else:
        with st.spinner("Fetching flight status..."):
            time.sleep(1.5)

        flight = FLIGHT_DB.get(flight_number)

        if not flight:
            st.error("No flight found for this number.")
        else:
            st.success(f"Status for {flight_number}")

            st.markdown("### ✈️ Flight Details")
            st.write(f"**Airline:** {flight['airline']}")
            st.write(f"**Status:** {flight['status']}")
            st.write(f"**Route:** {flight['departure']} → {flight['arrival']}")
            st.write(f"**Departure:** {flight['departure_time']}")
            st.write(f"**Arrival:** {flight['arrival_time']}")

            # Status indicator
            if flight["status"] == "On Time":
                st.success("🟢 On Time")
            elif flight["status"] == "Delayed":
                st.warning("🟡 Delayed")
            else:
                st.error("🔴 Unknown Status")