"""
Practical 08
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Constructs App class"""

    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Event handler for greeting."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def clear_greet(self):
        """Event handler for clearing greeting.."""
        self.root.ids.output_label.text = 'Hello '


BoxLayoutDemo().run()
