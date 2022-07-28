
from kivy.app import App
from kivy.uix.label import Label

class MyProg(App):

    def build(self):
        lb=Label()
        lb.text="Hello World"

        return lb




MyProg().run()




