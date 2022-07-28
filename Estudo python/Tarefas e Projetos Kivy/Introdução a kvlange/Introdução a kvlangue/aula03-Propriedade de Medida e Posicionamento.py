"""
FOI FEITO NO PROJETO KIVY
"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput


class Root(FloatLayout):
    pass

class myprog(App):

    def build(self):
        return Root()



Window.size=518,600
myprog.title="MEU PROGRAMA"
myprog().run()