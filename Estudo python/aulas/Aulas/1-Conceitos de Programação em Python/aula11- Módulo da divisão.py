"""
MÓDULO DA DIVISÃO

Serve para se obter o resto de uma divisão por eexemplo:

6%2 = 2 2 2 = 0
3%2 = 2 = 1 esse é o resto que sobrou  pois não cabe mais um dois dentro
8%2 = 2 2 2 2 = 0
16%5 = 5 5 5 = 1
7%3.1


"""





#print(3%2)

#print (6%2 )
#print (3%2 )
#print (6%2 )
#print (8%2 )
#print (16%5 )
#print (7%3.1 )
#print (900%100==0 )





num1 = float(input("Digite um número: "))#O FLOAT NA FRENTE DO INPUT SERVE PARA DEFINIR QUE O VALOR QUE IRA DIGITAR IRA SE TRANFORMAR EM NUMERO
num2 = float(input("Digite outro número: "))
print()

divisao = num1 / num2
resto = num1 % num2

print (num1, "dividido por", num2, "é igual a: ",divisao)
print ("O resto da divisão entre", num1, "e", num2 , "é igual a:",resto)