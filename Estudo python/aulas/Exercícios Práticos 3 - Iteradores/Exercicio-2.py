"""

2) Evolua o algoritmo no qual imprimimos os números num
intervalo pré-definido para um algoritmo que pergunte ao
 usuário qual o intervalo que o mesmo deseja que seja impresso:

"""

print()
print("Informe abaixo o inicio e fim do intervalo no qual deseja ser exibido!!")
print()

ped1= int(input("Informe o número inicial:"))
ped2= int(input("Informe o número final:"))


for lista in range(ped1,ped2):
    print(lista)