"""

Faça um algoritmo que solicite ao usuário informar o valor de uma compra.
Em seguida, aplique 10% de desconto e
imprima na tela tanto o valor total
e também o valor com o desconto aplicado.




"""

cpra=float(input("Informe o valor da compra:"))


total=cpra*10/100

totaldesc=cpra-total


print("O valor total da compra é: %s"%cpra)
print()
print("O valor total da compra com o desconto de 10 porcento é de: %s"%totaldesc)
