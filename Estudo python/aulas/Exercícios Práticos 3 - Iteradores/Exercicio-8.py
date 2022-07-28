"""


8) Faça um algoritmo que imprima os valores no intervalo definido pelo usuário e permita que o
 mesmo possa definir 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela:


"""

print("INFORME ABAIXO O INTERVALO DE NÚMEROS QUE SERÃO IMPRESSOS:")

start=int(input("Informe o número inicial:"))
end=int(input("Informe o número final:"))


print()
print("AGORA INFORME TRÊS NÚMERO QUE SERÃO IGNORADOS:")

num1=int(input("Primeiro número a ser ignorado:"))
num2=int(input("Segundo número a ser ignorado:"))
num3=int(input("Terceiro número a ser ignorado:"))


for top in range(start,end+1):
    if (top==num1) or (top==num2) or (top==num3):
        continue
    print(top)