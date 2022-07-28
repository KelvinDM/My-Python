"""
14) Escreva uma função que calcule o fatorial de um número
(um inteiro não negativo).
Envie o valor do número que será calcula
como argumento da função.

"""

func=int(input("Informe um número para exibir o fatorial:"))

#FUNÇÃO PARA CALCULO FATORIAL.
def fatorial(func):
    calc = 1
    for rex in range(func,0,-1):
        calc= calc*rex

    return calc

print(fatorial(func))
