
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


code="""
BoxLayout:
    Button:
        text:"1"
    Button:
        text:"2"

"""

from kivy.lang import Builder

class Estudo6App(App):
    def build(self):
        return Builder.load_string(code)


janela = Estudo6App()
janela.run()