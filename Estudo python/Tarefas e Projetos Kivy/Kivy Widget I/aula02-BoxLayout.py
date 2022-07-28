#coding: utf-8
#author: Kelvin Daniel Martins de Araujo


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder




kvcode="""
BoxLayout:
    orientation:"vertical"
    padding:20
    spacing:50
    Button:
        size_hint:1., 1.
        # pos_hint:{"x":0, "top":1.}
        text:"A"
    Button:
        size_hint:1.,1.
        text:"B"
    Button:
        size_hint:1.,1.
        text:"C"
    
"""







class JanelaApp(App):
    def build(self):

        return Builder.load_string(kvcode)



janela=JanelaApp()
janela.run()