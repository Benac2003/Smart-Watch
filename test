from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
import random

class YourWidget(Widget):
    random_number = StringProperty()

    def __init__(self, **kwargs):
        super(YourWidget, self).__init__(**kwargs)
        self.random_number = str(random.randint(1, 100))

    def change_text(self):
        self.random_number = str(random.randint(1, 100))

class YourApp(App):
    def build(self):
        return YourWidget()

if __name__ == '__main__':
    YourApp().run()