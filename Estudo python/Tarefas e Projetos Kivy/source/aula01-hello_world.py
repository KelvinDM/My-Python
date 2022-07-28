#conding:utf-8

from  kivy.app import App
from kivy.uix.label import Label


class meuprog(App):

    def build(self):
        return Label(text="Hello Wold")





meuprog().run()