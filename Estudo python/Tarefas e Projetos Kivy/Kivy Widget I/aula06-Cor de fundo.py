# coding: utf-8
# author: Kelvin Daniel Martins de Araujo


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.utils import get_color_from_hex
from kivy.core.window import Window

#Utilizado toda vez para limpar o video do kivy
# Window.clearcolor=[1,1,1,1] #deixa branco
Window.clearcolor= get_color_from_hex("#483D8B") #cor de funco em exadecimal



kvcode = """
#:import C kivy.utils.get_color_from_hex

<Fverde@FloatLayout>:
    size_hint:.3,.3
    
    canvas.before:
        Color:
            rgba: C("#00FF00")
        Rectangle:
            pos:self.pos
            size:self.size    

FloatLayout:
    Fverde:
        pos_hint:{"x":.4,"y":.4}
    Button:
        size_hint:.3,.3
        pos_hint:{"center_x":.5,"center_y":.5}
        # background_color:0,.2,.1,1
        background_color: C ("#87CEEB")
        background_normal:""
        text:"Me APERTE"
        


# FloatLayout:
#     Button:
#         size_hint:.3,.3
#         pos_hint:{"center_x":.5,"center_y":.5}
#         # background_color:0,.2,.1,1
#         background_color: C ("#87CEEB")
#         background_normal:""
"""


class JanelaApp(App):
    def build(self):
        return Builder.load_string(kvcode)


janela = JanelaApp()
janela.run()

