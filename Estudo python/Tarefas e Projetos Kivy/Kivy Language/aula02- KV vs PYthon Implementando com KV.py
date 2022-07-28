from tkinter import Widget

import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button



class Tela1(BoxLayout):

    def on_press_botao(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela2())

class Tela2(BoxLayout):

    def on_press_botao(self):
        janela.root_window.remove_widget(janela.root)
        janela.root_window.add_widget(Tela1())


class KVvsPY2(App):
    pass
    # def build(self):
    #     return Tela1()
    #Posso utilizar a mesma chamada de tela no KV colocando apenas o nome da tela.

janela=KVvsPY2()
janela.run()














