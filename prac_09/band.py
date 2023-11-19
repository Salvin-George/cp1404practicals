"""
Band class
Estimate: 20mins
Actual: 19mins
"""


class Band:
    """Constructs Band object."""
    def __init__(self, name=''):
        """Initialises band object."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Adds musician to musicians"""
        return self.musicians.append(musician)

    def __str__(self):
        """Represents """
        return f"{self.name} ({self.musicians})"

    def play(self):
        for musician in self.musicians:
            print(musician.play())