"""

   DESEMPACOTAMENTO

É a extração dos elementos contidos
numa estrutura


"""
#Os número 10 e 20 será empacotados para a variavel lista
lista=[10,20]


def func (a,b):
    print()
    func(*lista)
    func(10,20)
    func(a=10,b=20)
x,y=lista


def pessoa(nome,sobrenome,idade):
    print(nome)
    print(sobrenome)
    print(idade)

# lista= ["eXcript","Brasil",20]

#pessoa(tupla[0],tupla[1],tupla[2])
# pessoa(*lista)

d = {"sobrenome":"Brasil","idade":20,"nome":"eXcript"}

pessoa(**d) #**utilizado em dicionarios