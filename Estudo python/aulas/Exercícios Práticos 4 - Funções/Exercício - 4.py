"""



4) Escreva um algoritmo contendo uma função que necessite de
três argumentos. Em seguida, imprima na tela os argumentos em
ordem ascendente e, por fim, imprima a média aritmética:
"""

result=0
lista=[11,10,12]

def legal(a,b,c):
    print(a)
    print(b)
    print(c)

lista.sort()

legal(*lista)
#---------------------------------------------------------------------------------
top=lista[0]+lista[1]+lista[2]
media=top/3
print("O valor total: ",media)
