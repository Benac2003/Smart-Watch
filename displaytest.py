import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.core.window import Window

class CustomPopup(Popup):
    pass

class CustFloatLayout(FloatLayout):
    checkbox_is_active = ObjectProperty(False)

    def switch_on(self, instance, value):
        if value is True:
            print("switch on")
        else:
            print("switch of")
    
    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()

class Main_App(App):
    def build(self):
        Window.clearcolour = (1,1,1,1)
        return CustFloatLayout()

Smart_Watch = Main_App()
Smart_Watch.run()