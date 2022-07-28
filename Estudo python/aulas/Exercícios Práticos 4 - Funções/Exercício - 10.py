"""


10) Escreva um algoritmo que encontre o maior dentre 3 números.
Para facilitar a resolução do exercício utilize funções.

"""

lista=[11,10,12]

def legal(a,b,c):
    print(a)
    print(b)
    print(c)

lista.sort()

legal(*lista)

print("Dentre os três números o maior é:",lista[2])
