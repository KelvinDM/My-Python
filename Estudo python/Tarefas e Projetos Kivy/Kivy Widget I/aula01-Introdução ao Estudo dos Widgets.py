#coding: utf-8
#author: Kelvin Daniel Martins de Araujo

from kivy.app import App
from kivy.uix.button import Button
# from kivy.interactive import InteractiveLauncher
from kivy.lang import Builder



kvcode= """
FloatLayout:
    Button:
        size_hint:.1, .1
        pos_hint:{"x":0, "top":1.}
        text:"A"
    Button:
        size_hint: .2,.2
        pos_hint:{"center_x":.5,"center_y":.5}
        text:"B"
    Button:
        size_hint:.1,.1
        pos_hint:{"y":0,"right":1.}
        text:"C"
    Button:
        size_hint:None,None
        pos_hint:{"center_y":.7}
        x:150
        width:200
        heigth:100
        text:"absoluto"
"""

class JanelaApp(App):
    def build(self):
        return Builder.load_string(kvcode)


janela=JanelaApp()
janela.run()