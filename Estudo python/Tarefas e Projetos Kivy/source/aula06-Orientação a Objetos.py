#conding:utf-8

from kivy.app import App
from kivy.uix.label import Label

class myprog(App):

    def build(self):
        lb = Label()
        lb.text = "Olá Vou me tornar um programador"


        return lb


myprog().run()