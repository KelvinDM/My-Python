a = 25 # Ele não ira puxar o 25 pois dentro do primeiro IF a variavel A esta recebendo 50

if(True):
    a = 50
    if(False):
        b = 50
    a = 40

    print(a)

"""
Ele vai imprimir o número 40 pois a variavel A esta na mesma linha hierarquica do primneiro IF, porém se ele estivesse na mesma linha de instrução do segundo IF ele não seria executado

"""