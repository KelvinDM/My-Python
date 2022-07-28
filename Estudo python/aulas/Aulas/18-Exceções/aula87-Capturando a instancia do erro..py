"""

EXCEÇÕES

Capturando a Instância do erro

utlizando a intrução 'as' para capturar informações
do traceback
"""

def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print("ValueError")
        print(type(e))#instância da execeção
        print(e.args)#argumentos as mensagens
        print(e)#__str__mensagem
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except (TypeError,NameError) as e: #Dessa maneira consigo colocar varias exceções
        print(type(e))#instância da execeção
        print(e.args)#argumentos as mensagens
        print(e)#__str__mensagem



#TypeError
erro("int+int")

#NameError
erro("a")

#ValueError
# erro("int('a')")

#ZeroDivisionError
# erro("5/0")
# erro("10+10")
print("A aplicação foi finalizada.")