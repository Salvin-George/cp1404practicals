"""
Taxi class test
Estimate: 10mins
Actual:
"""
import prac_09.taxi


def main():
    """Test taxi class."""
    my_taxi = prac_09.taxi.Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()
