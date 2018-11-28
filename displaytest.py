import kivy
kivy.require("1.9.0")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.pagelayout import PageLayout
from kivy.properties import NumericProperty
class GUI(PageLayout):
    pass

class Main_App(App):
    hour = 10
    def build(self):
        return GUI()

Smart_Watch = Main_App()
Smart_Watch.run()