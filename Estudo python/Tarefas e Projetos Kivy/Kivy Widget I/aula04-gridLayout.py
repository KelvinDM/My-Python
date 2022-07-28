#coding: utf-8
#author: Kelvin Daniel Martins de Araujo


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder


kvcode="""
GridLayout:
    cols:3
    rows:None
    
    row_default_height:50
    row_force_default:True
    
    # col_default_width:50
    # col_force_default:True
    
    Button:
        text:"A"
        size_hint:.3,None
    Button:
        text:"B"
    Button:
        text:"C"
    Button:
        text:"D"
        size_hint:.3,None
    Button:
        text:"E"
    Button:
        text:"F"
    Button:
        text:"G"
        size_hint:.3,None



"""






class JanelaApp(App):
    def build(self):
        return Builder.load_string(kvcode)




janela=JanelaApp()
janela.run()
