import kivy
kivy.require("1.9.0")
from kivy.app import App
from kivy.uix.widget import Widget
class Lockscreen(Widget):
    pass

class Main_App(App):
    
    def build(self):
        return Lockscreen()

Smart-Watch = Main_App()
Smart-Watch.run()