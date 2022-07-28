
#Escopo: São regiões onde uma determinada variavel pode ser acessada.

a=1
b=2

def soma(var1,var2):
    s=var1+var2
    return  s

def imprime(x_vezes):
    for i in range (x_vezes):
        print(i)

print(soma(a,b))
imprime(5)