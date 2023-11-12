"""
Practical 08
Estimated: 15mins
Actual:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to generate labels based of names."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ['Robert', 'John', 'Michael', 'David', 'William', 'Jeff']

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            temp_button = Label(text=name)
            self.root.ids.main.add_widget(temp_button)
        return self.root


DynamicLabelsApp().run()
