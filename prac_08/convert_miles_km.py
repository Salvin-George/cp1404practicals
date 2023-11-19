"""
Prac 07
Estimate: 25mins
Actual: 30mins
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILESTOKM = 1.60934


class MilestoKmApp(App):
    """Kivy app to convert from miles to Kilometers"""
    output = StringProperty()

    def build(self):
        """Builds Kivy App"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output = "Type in the field & press Enter"
        return self.root

    def get_valid_input(self):
        """Error checks input of app"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0

    def handle_calculation(self):
        """Changes display to show calculations"""
        self.output = str(self.get_valid_input() * MILESTOKM)

    def handle_increment(self, change):
        """Increases current values by +/- 1"""
        self.root.ids.input_miles.text = str(self.get_valid_input() + change)
        self.handle_calculation()


MilestoKmApp().run()
