"""

SISTEMA DE POSICIONAMENTO


"""



from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class myprog(App):

    def build(self):
        layout=FloatLayout()
        bt=Button()
        bt.size_hint = None, None
        bt.text="Clique aqui"
        bt.width=85
        bt.height=85
        bt.y=300 #Quantidade de Y é para cima
        bt.x=350 #Quantidade de X é para a direita



        layout.add_widget(bt)

        return layout

myprog.title="Meu programa. ver.0.01"
Window.size=600,600
myprog().run()


