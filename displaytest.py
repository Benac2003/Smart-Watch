
#kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.lang import *
from StoringVariables import *

#update time and date

#Imports data from app.kv
class Lockscreen(Widget):
    def Updatetime(self, **kwargs):
        super(Lockscreen, self).Updatetime(**kwargs)
    def change_text(self):
        #update time
  

#builds gui
class app(App):
    def build(self):
        return Lockscreen()
app().run()

