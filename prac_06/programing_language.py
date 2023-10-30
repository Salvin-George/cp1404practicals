"""
Languages Class file
Estimate: 10mins
Actual:
"""


class ProgrammingLanguage:
    """Represents information about a programing langauge."""

    def __init__(self, name, typing, reflection, year):
        """Initialises class variables."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determines if programing is dynamically typed."""
        return self.typing == "Dynamic"

