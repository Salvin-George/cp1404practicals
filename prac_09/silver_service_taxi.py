"""
Silver service taxi class
Estimate: 20mins
Actual:11mins
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Intialises a SilverServiceTaxi object."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get current fare."""
        return self.flagfall + super().get_fare()
