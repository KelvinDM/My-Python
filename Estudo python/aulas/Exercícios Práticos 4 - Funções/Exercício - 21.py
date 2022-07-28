"""

21) Escreva uma função que tenha definida uma função em seu escopo.
Invoque a função aninhada, retorne algum valor,
 imprima esse valor na tela e finalize a aplicação.

"""
x=10
def func():


    def func_interna():
        print("FUNÇÃO INTERNA:",x)

    func_interna()


func()