#coding: utf-8
#author: Kelvin Daniel Martins de Araujo

from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.lang import Builder



kvcode="""
StackLayout:
    orientation:"bt-lr"
    Button:
        text:"A"
        size_hint:.33,.1
    Button:
        text:"B"
        size_hint:.33,.1
    Button:
        text:"C"
        size_hint:.33,.1
        

"""





class JanelaApp(App):
    def build(self):
        return Builder.load_string(kvcode)



janela=JanelaApp()
janela.run()

