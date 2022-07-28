"""

FUNÇÃO VARIÁDICA

É toda função capaz de receber quantidades
arbitrárias de parâmetros


"""
#Quando informao * na frente da função varivel podemos associar uma lista a ela
def lista_de_argumentos(*lista):#LISTA
    print(lista)


#Quando informao ** na frente da função varivel podemos associar um dicionario
def lista_de_argumentos_associativos(**dicionario):#DICIONARIO
    print(dicionario)



def argumentos(*lista,**dicionario):
    print(lista)
    print(dicionario)

argumentos(1,2,3,4,um=1, dois=2, tres=3)


# lista_de_argumentos(1,2,3,4,5,6)
# lista_de_argumentos("Um","Dois","TRês","Quatro")


# lista_de_argumentos_associativos(a=1,b=2,c=3,d=4)
# lista_de_argumentos_associativos(um=1,dois=2,tres=3,quatro=4)

