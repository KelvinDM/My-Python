#8) Faça um algoritmo que peça dois números. Primeiro, imprima o maior e, em seguida, o menor.


num1= int(input("Digite o primeiro número:"))
num2= int(input("Digite o segundo número:"))



if (num1>num2):
    print("O Maior número é %i e o menor número é %i" %(num1,num2))
else:
    if(num2>num1):
        print("O Maior número é %i e o menor número é %i" %(num2,num1))