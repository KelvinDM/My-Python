#coding: utf-8
#author: Kelvin Daniel Martins de Araujo


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.utils import get_color_from_hex
get_color_from_hex("#FFFFFF")

kvcode="""
#:import C kivy.utils.get_color_from_hex

FloatLayout:
    Button:
        size_hint:.3,.3
        pos_hint:{"center_x":.5,"center_y":.5}
        # background_color:0,.2,.1,1
        background_color: C ("#FFD700")
        background_normal:""
    


"""



class JanelaApp(App):
    def build(self):
        return Builder.load_string(kvcode)



janela=JanelaApp()
janela.run()

