"""
17) Escreva uma função que receba como argumento uma lista que poderá
ter valores duplicados e retorne uma nova lista sem que haja valores iguais.
Lista: [1,2,3,3,3,3,4,5]
Retorno: [1, 2, 3, 4, 5]


"""

lista = [1,2,3,3,3,3,4,5]

resultlist = []

for elemento in lista:
    if elemento not in resultlist:
        resultlist.append(elemento)

print(resultlist)