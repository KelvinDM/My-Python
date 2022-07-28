#4) Faça um algoritmo que peça a idade de uma pessoa e imprima na tela se a mesma já é maior de idade ou então, se a mesma é de menor.

idade = int(input("Informe sua idade:"))


if (idade>18):
    print("Você possui %i anos de idade e já é de maior!!!" %(idade))
else:
    print("Você possui %i anos de idade e ainda é de menor!!!" %(idade))