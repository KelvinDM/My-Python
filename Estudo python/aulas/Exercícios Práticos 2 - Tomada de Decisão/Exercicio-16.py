"""
16) Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E. Os endereços no intervalo
de 0 à 127 são classe A, de 128 a 191 são classe B, de 192 a 223 são
 classe C, de 224 à 239 são classe D e a partir de 240 são classe E.
Faça um algoritmo que leia o primeiro octeto, no formato decimal de um endereço IP, e informe a sua classe.
"""

num1= float(input("Digite o IP:").split('.')[0])# [] lista ta posições

if (num1<=127):
    print("A Classe do IP é A.")

if (num1>=128) and (num1<=191):
    print("A Classe do IP é B")

if (num1>=192) and (num1<=223):
    print("A Classe do IP é C")

if (num1>=224) and (num1<=239):
    print("A Classe do IP é D")

if (num1>=240):
    print("A Classe do IP é E")





