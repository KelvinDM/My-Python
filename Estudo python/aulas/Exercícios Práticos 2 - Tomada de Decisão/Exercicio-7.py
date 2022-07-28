#7) Faça um algoritmo que peça um número ao usuário e verifique se o mesmo é par ou então ímpar.


num1 = int(input("Digite um número por gentileza:"))

num2 =num1%2

if (num1%2)==0: # Serve para verificar o resto da divisão do número
    print("O número %i é impar" %(num1))
else:
    print("O número %i é par" %(num1))


print("valor do número na variavel é: %i." %(num2))