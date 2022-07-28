""""
20) Escreva uma função que verifica se
uma String enviada é um palíndromo ou não.


"""

mundo = input("Informe uma palavra:")
if (mundo) == (mundo)[::-1] :# Determinando desta maneira consigo verificar a mesma palavra de tràs para frente
    print("Essa palavra é um Palindrome!!")
else:
    print("Essa palavra não é um Palindrome!!")