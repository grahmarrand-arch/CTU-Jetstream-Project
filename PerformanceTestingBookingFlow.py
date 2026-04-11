from locust import HttpUser, task, between
import random


class BookingPaymentUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        """Login once per virtual user"""
        response = self.client.post("/api/login", json={
            "email": "testuser@example.com",
            "password": "password123"
        })

        self.token = None
        self.booking_id = None

        if response.status_code == 200:
            self.token = response.json().get("token")

    def headers(self):
        return {
            "Authorization": f"Bearer {self.token}"
        } if self.token else {}

    @task(3)
    def search_flights(self):
        """Search available flights (high frequency task)"""
        self.client.get(
            "/api/flights/search?from=NYC&to=LAX&date=2026-05-01",
            headers=self.headers()
        )

    @task(2)
    def create_booking(self):
        """Create booking"""
        payload = {
            "flight_id": random.randint(1, 100),
            "seat_class": "economy",
            "passengers": 1
        }

        response = self.client.post(
            "/api/booking/create",
            json=payload,
            headers=self.headers()
        )

        if response.status_code == 200:
            try:
                self.booking_id = response.json().get("booking_id")
            except:
                self.booking_id = None

    @task(2)
    def process_payment(self):
        """Process payment for booking"""
        if not self.booking_id:
            return

        payload = {
            "booking_id": self.booking_id,
            "payment_method": "card",
            "amount": 350
        }

        self.client.post(
            "/api/payment/process",
            json=payload,
            headers=self.headers()
        )

    @task(1)
    def check_booking_status(self):
        """Check booking status"""
        self.client.get(
            "/api/booking/status",
            headers=self.headers()
        )