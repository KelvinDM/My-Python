#14) Faça um algoritmo que leia três números e imprima-os em ordem crescente.

print(50*"-")
print("Informe três números abaixo:")
print(50*"-")


num1=int(input("Informe o primeiro número:"))
num2=int(input("Informe o segundo número:"))
num3=int(input("Informe o terceiro número:"))


if (num1>=num2) and (num1>=num3):
    print(" A sequencia em ordem crescente é: %i, %i, %i." %(num3,num2,num1))
if (num2>=num1) and (num2>=num3):
    print(" A sequencia em ordem crescente é: %i, %i, %i." % (num1, num3, num2))
if (num3>=num1) and (num3>=num2):
    print(" A sequencia em ordem crescente é: %i, %i, %i." % (num1, num2, num3))

