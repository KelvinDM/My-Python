
"""
SISTEMAS DE MEDIDAS

px=Pixels
m=Polegadas
mm=Milímetros
pt=Ponto
dp=Pixel Independete de Densidade
sp=Escala Independente de Pixel

Resolução de Tela: É a quantidade de Pixel que
nossa tela é capaz de exibir

dpi:(dots per inch) ou pontos por polegadas é a
medida obtida pela divisão do tamanho fisíco do dusplay
em centímetros ou polegadas pela resolução em pixels.

tamanho Físico Display
----------------------- dividido
Resolução Pixels


Densidade de Pixel: é a quantidade de pixels
por polegada quadrada

largura da Tela(ou altura) em Pixel          Ipixel
----------------------------------------- = ---------
Largura da Tela (ou altura) em polegadas    Ipolegadas


             DP

Largura em Pixel*160    Ipixel
-------------------- = --------
Densidade da Tela         dt


dp  = sp


"""

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

class myprog(App):

    def build(self):
        layout=FloatLayout()
        bt=Button()
        bt.size_hint = None, None
        bt.text="Start"
        bt.height=60
        bt.width=150
        bt.y=10
        bt.x=300

        layout.add_widget(bt)
        return layout


myprog().run()
