"""
Unrealible car Class
Estimate: 10mins
Actual: 11mins
"""

from random import randint

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __repr__(self) -> str:
        """Return a string like a Car but with reliability rate (%)."""
        return f"{super().__str__()}, {self.reliability * 100}% reliable"

    def drive(self, distance) -> int:
        """Drive the car, based on reliability and a random chance of sucess."""
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
        total_distance = super().drive(distance)
        return total_distance
