"""
Client code for silver service taxi.
Estimate: 3mins
Actual: 2mins
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
