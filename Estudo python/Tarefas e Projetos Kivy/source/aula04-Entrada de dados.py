#conding:utf-8

from kivy.app import App
from kivy.uix.textinput import TextInput

class myprog(App):
    def build(self):
        # return TextInput(text="COMPONETE: TextInput")
        txt = TextInput()
        txt.text = "O começo de tudo:"
        txt.font_size = 25
        return txt




myprog().run()