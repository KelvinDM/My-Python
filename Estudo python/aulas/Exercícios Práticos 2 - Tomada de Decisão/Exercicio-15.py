#15) Faça um algoritmo que leia um caractere e informe se o mesmo é uma vogal ou não.


vogal=str(input("Digite uma letra:"))


if vogal in "aeiou":#A função IN é utilizada para colocar varias informações dentro de uma unica variavel
    print("A letra digitada é uma vogal.")
else:
    print("A letra digitada não é uma vogal.")



