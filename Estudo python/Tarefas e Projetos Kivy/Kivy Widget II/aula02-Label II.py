#coding: utf-8
#author: Kelvin Daniel Martins de Araujo


from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


kvcode="""
StackLayout:
    orientation:"tb-lr"
    padding:50
    Label:
        markup=True
        text:"Estudando a [b]classe[/b] Label"
        font_size: 30
        font_name: "consola"
        # italic:True
        bold: True
        color: .1,.2,.3,1

"""



class JanelaApp(App):
    def build(self):
        return Builder.load_string(kvcode)


janela=JanelaApp()
janela.run()


