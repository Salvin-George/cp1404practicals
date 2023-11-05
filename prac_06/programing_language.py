"""
Languages Class file
Estimate: 10mins
Actual: 8mins
"""


class ProgrammingLanguage:
    """Represents information about a programing langauge."""

    def __init__(self, name, typing, reflection, year):
        """Initialises class variables."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determines if programing is dynamically typed."""
        return self.typing == "Dynamic"

    def print_dyanmic_programs(self):
        python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
        ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
        visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

        languages = [python, ruby, visual_basic]

        print("The dynamically typed languages are:")
        for language in languages:
            if language.is_dynamic():
                print(language.name)
