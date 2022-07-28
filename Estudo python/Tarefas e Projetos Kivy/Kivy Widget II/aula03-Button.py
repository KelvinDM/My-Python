#coding: utf-8
#author: Kelvin Daniel Martins de Araujo


from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.interactive import InteractiveLauncher

janela=None
glayout=None



class JanelaApp(App):
    pass

janela=JanelaApp()
ji=InteractiveLauncher(janela)
ji.run()

kvcode="""
Button:
    text:"oi"


"""
# def add_bt(**args):
#     bt=Button(text="Estudando a classe Label",
#              size_hint_y=None,height=50,markup=True,**args)






class JanelaApp(App):
    pass



janela=JanelaApp()
janela.run()




