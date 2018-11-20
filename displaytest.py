
#kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.lang import *
from StoringVariables import *

#update time and date
def Time(ticks, hour, second, minute,day, month, year):
    time = "%02d : %02d : %02d" % (hour, minute, second)
    date = "%02d/%02d/%04d" % (day, month, year)
    return time, date

#Imports data from app.kv
class Lockscreen(Widget):
    time = StringProperty()
    def Updatetime(self, **kwargs):
        super(Lockscreen, self).Updatetime(**kwargs)
    def change_text(self):
        #update time
        ticks, hour, minute, second, day, month, year, pm = Data_get()
        self.time = self.time = "%02d : %02d : %02d" % (hour, minute, second)

#builds gui
class app(App):

    def build(self):
        return Lockscreen()
app().run()

