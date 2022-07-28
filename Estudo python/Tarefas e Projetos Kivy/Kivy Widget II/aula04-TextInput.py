#coding: utf-8
#author: Kelvin Daniel Martins de Araujo


from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher



kvcode="""
FloatLayout:
    TextInput:
        id:text_input
        size_hint:None,None
        text:"MEU PROGRAMA"
        width:root.width
        height:root.height
        font_size:20
        foreground_color:.2,.1,1
        #write_tab: False #Desliga o TAB
        padding_x: 25
        # readonly:True #Liga o modo leitura(não deixa escrever)
        # font_name:"consola" #Mudar o estilo da fonte
"""


class JanelaApp(App):
    def build(self):
        return Builder.load_string(kvcode)


janela=JanelaApp()
janela.run()


