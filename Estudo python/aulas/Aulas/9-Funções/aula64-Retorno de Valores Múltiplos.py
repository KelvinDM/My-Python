"""

    RETORNO DE VALORES MÚLTIPLOS

Muito importante para retornar tuplas ou listas
para funções


"""


def func():
    return 1,2 #O valor retornado se tornara uma tupla


a,b=func()

print(a)
print(b)
print(50*"-")


def potencia(x):
    quadrado=x**2
    cubo=x**3

    return quadrado,cubo

q,c=potencia(10) #Foram atribuidos quadrado e cubo :D

print(q)
print(c)