import streamlit as st
from datetime import date

st.title("✈️ Multi-City Flight Booking")

# Initialize session state
if "legs" not in st.session_state:
    st.session_state.legs = [
        {"from": "", "to": "", "date": date.today()}
    ]

# Add new leg
def add_leg():
    st.session_state.legs.append({"from": "", "to": "", "date": date.today()})

# Remove leg
def remove_leg(index):
    if len(st.session_state.legs) > 1:
        st.session_state.legs.pop(index)

st.subheader("Your Trip")

for i, leg in enumerate(st.session_state.legs):
    st.markdown(f"### Segment {i + 1}")

    col1, col2, col3, col4 = st.columns([3, 3, 3, 1])

    with col1:
        leg["from"] = st.text_input(
            "From",
            value=leg["from"],
            key=f"from_{i}"
        )

    with col2:
        leg["to"] = st.text_input(
            "To",
            value=leg["to"],
            key=f"to_{i}"
        )

    with col3:
        leg["date"] = st.date_input(
            "Date",
            value=leg["date"],
            key=f"date_{i}"
        )

    with col4:
        if st.button("❌", key=f"remove_{i}"):
            remove_leg(i)
            st.rerun()

st.divider()

colA, colB = st.columns(2)

with colA:
    if st.button("➕ Add Destination"):
        add_leg()
        st.rerun()

with colB:
    if st.button("🔍 Search Flights"):
        st.success("Searching multi-city flights...")

        for i, leg in enumerate(st.session_state.legs):
            st.write(
                f"Segment {i+1}: {leg['from']} → {leg['to']} on {leg['date']}"
            )