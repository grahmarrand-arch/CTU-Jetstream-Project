# main.py

"""
Main entry point for Airline Booking System
This file connects all modules and simulates system workflow.
"""

# Import all modules
import SeatMapUIDesign
import BackendAPISeatAvailability
import LockSeatAfterPayment
import CancelBookingButton
import RefundViaAPIIntegration
import RefundCalculationLogic
import BookingHistoryUIDesign
import ConnectDashboardtoAPI
import FlightStatusUIDesign
import FlightStatusAPIIntegration
import FlightStatusDisplay
import MultiCityBookingUI
import ItineraryBuilderLogic
import TravelSequenceValidation
import MultiLegPaymentWorkflow
import RBACImplementation
import EditFlightDetails
import UpdatePropagationToSearch
import PerformanceTestingBookingFlow
import CachingForSearchResults
import PenetrationTestingOverview
import ErrorHandingImprovemntTips


def run_demo():
    print("✈️ Airline Booking System Started...\n")

    # 1. Validate Travel Plan
    print("🔍 Validating travel sequence...")
    TravelSequenceValidation.validate()

    # 2. Build Itinerary
    print("🧭 Building itinerary...")
    itinerary = ItineraryBuilderLogic.build()

    # 3. Show Multi-city UI
    print("🌍 Multi-city booking UI...")
    MultiCityBookingUI.display()

    # 4. Seat Availability
    print("💺 Checking seat availability...")
    BackendAPISeatAvailability.check()

    # 5. Seat Map UI
    print("🪑 Rendering seat map...")
    SeatMapUIDesign.render()

    # 6. Lock Seat After Payment
    print("🔒 Locking seat after payment...")
    LockSeatAfterPayment.lock()

    # 7. Payment Workflow
    print("💳 Processing multi-leg payment...")
    MultiLegPaymentWorkflow.process()

    # 8. Booking History
    print("📜 Display booking history...")
    BookingHistoryUIDesign.show()

    # 9. Flight Status
    print("🛫 Fetching flight status...")
    FlightStatusAPIIntegration.fetch()
    FlightStatusDisplay.show()

    # 10. Dashboard API Connection
    print("📊 Connecting dashboard...")
    ConnectDashboardtoAPI.connect()

    # 11. Cancel Booking
    print("❌ Cancel booking...")
    CancelBookingButton.cancel()

    # 12. Refund Logic
    print("💰 Calculating refund...")
    RefundCalculationLogic.calculate()

    print("💸 Sending refund...")
    RefundViaAPIIntegration.process()

    # 13. Admin RBAC
    print("🔐 Checking admin permissions...")
    RBACImplementation.check_access()

    # 14. Edit Flight
    print("✏️ Editing flight details...")
    EditFlightDetails.edit()

    # 15. Update Search Cache
    print("🔄 Updating search results...")
    UpdatePropagationToSearch.update()

    # 16. Caching
    print("⚡ Using cache for search...")
    CachingForSearchResults.cache()

    # 17. Performance Test
    print("📈 Running performance tests...")
    PerformanceTestingBookingFlow.test()

    # 18. Security Testing
    print("🛡️ Running penetration tests...")
    PenetrationTestingOverview.run()

    # 19. Error Handling Demo
    print("⚠️ Testing error handling...")
    ErrorHandingImprovemntTips.demo()

    print("\n✅ System execution completed successfully!")


if __name__ == "__main__":
    run_demo()