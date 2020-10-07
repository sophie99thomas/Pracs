"""
Program that converts miles to kilometres.
CP1404 - Practical 7
Sophie Thomas.
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

CONVERSION_FACTOR = 1.609


class MilesToKm(App):
    message = StringProperty()

    def build(self):
        self.title = "Converter Program"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, amount):
        MilesToKm.empty_box_check(self)
        self.root.ids.miles_input.text = str(int(self.root.ids.miles_input.text) + amount)

    def input_check(self):
        miles_input = str(self.root.ids.miles_input.text)
        if miles_input.isdigit():
            MilesToKm.convert(self)
        else:
            self.root.ids.output_label.text = "Please enter a valid number"

    def convert(self):
        self.message = self.root.ids.miles_input.text
        self.root.ids.output_label.text = str(int(self.root.ids.miles_input.text) * CONVERSION_FACTOR)

    def empty_box_check(self):
        box_text = str(self.root.ids.miles_input.text)
        if box_text == "" or box_text == " ":
            self.root.ids.miles_input.text = "0"


MilesToKm().run()
