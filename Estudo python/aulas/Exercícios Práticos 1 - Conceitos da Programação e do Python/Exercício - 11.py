"""

 Faça um algoritmo que solicite ao usuário digitar 2 números.
 Em seguida, imprima o
  total decimal da divisão e o
  total inteiro (sem casas decimais):


"""

num1=float(input("Informe o primeiro número:"))
num2=float(input("Informe o segundo número:"))

div=num1 / num2


print(" %s dividido por %s é igual ao total decimal: %s" %(num1,num2,div))
print(" %s dividido por %s é igual ao total inteiro: %0.f" %(num1,num2,div))