"""
Guitar class
Estimate:10mins
Actual:11mins
"""
CURRENT_YEAR = 2023


class Guitar:
    """Creates a Guitar class object for storing details."""

    def __init__(self, name="", year=0, cost=0):
        """Initialises a Guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __lt__(self, other):
        return self.year < other.year

    def __str__(self):
        """Returns a string representation of Guitar object"""
        return f"{self.name} ({self.year}): ${self.cost:,.2f}"

    def get_age(self):
        """Gets current age of Guitar based on CURRENT_YEAR"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determines if guitar object is vintage"""
        return self.get_age() > 50
