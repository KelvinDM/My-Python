#conding:utf-8


from kivy.app import App
from kivy.uix.button import Button

var=0
def click():
    print("O botão foi clicado.")

class myprog(App):
    def build(self):
        # return Button(text="Opa clica em MIM!")#teste1
        bt = Button(text="Clique aqui")  # teste2
        bt.on_press = click
        return bt


myprog().run()