"""

Instrução NONLOCAL

É a instrução que permite acessar membros
não globais e não locais, membros
contidos no escopo externo

"""

a=0

def func1():
    b=0
    def func2():
        nonlocal b #nonlocal permite acessar uma variavel que não está no escopo local
        b=5


# def func():
#
#     var_local=10
#     def func_interna():
#         nonlocal var_local
#         var_local+=1
#         print(var_local)
#
#     func_interna()
# func()


z=2000
def vida():
    x=10


    def funcX():
        nonlocal x#se eu utilizar a variavel 'nonlocal' ele vai puxar a função local do escopo
        global z#se eu utilizar a variavel 'global' ele vai puxar defora da função
        print(x)
        print(z)
    funcX()
vida()