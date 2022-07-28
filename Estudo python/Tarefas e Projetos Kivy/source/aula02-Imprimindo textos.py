#conding:utf-8

"""

from kivy.app import App
from kivy.uix.label import Label

def build():
    # return Label(text="Estou aprendendo", italic=True, font_size=20)
    lb=Label()
    lb.text="Curso de Python e Kivy"
    lb.italic=True
    lb.font_size=50
    return lb



iniapp=App()
iniapp.build=build
iniapp.run()
"""

from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
Window.size=518,600


class myprog(App):
    def build(self):
        layout = FloatLayout()

        txt = TextInput()
        txt.size_hint = None, None
        txt.text = "BEM VINDO:D"
        txt.font_size = 50
        txt.height = 300
        txt.width = 400
        txt.x = 60
        txt.y = 250

        bt=Button()
        bt.size_hint=None,None
        bt.text="Clique Aqui."
        bt.font_size=25
        bt.height=50
        bt.width=150
        bt.x = 180
        bt.y = 130




        layout.add_widget(txt)
        layout.add_widget(bt)

        return layout




myprog.title="myprog Ver:0.01"
myprog().run()