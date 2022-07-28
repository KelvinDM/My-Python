"""

19) Escreva uma função que imprima somente os números pares
Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Saída: [2, 4, 6, 8]




"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

resultlist = []

for elemento in lista: #Oque estiver despois do in sempre será adicionado na variavel 'elemento'
    if (elemento % 2 == 0):
        resultlist.append(elemento)
        #Aqui está sendo adicionado os elementos da lista um por um  devico a função .append


print(resultlist)