"""


Execeções

Tratamento de Mútltiplas exceções


Nessa aula aprendi que conseguimos colocar varias traceback
dentro das execeções utilizando parenteses

exemplo:

    try:
        eval(x)
    except (TypeError,NameError,ValueError,ZeroDivisionError)

"""


def erro(x):
    try:
        eval(x)
    except (TypeError,NameError): #Dessa maneira consigo colocar varias exceções
        print("NameError ocorreu ou então,TypeError")
    except NameError:
        print("NameError")
    except ValueError:
        print("ValueError")
    except ZeroDivisionError:
        print("ZeroDivisionError")


#TypeError
erro("int+int")

#NameError
erro("a")

#ValueError
erro("int('a')")

#ZeroDivisionError
erro("5/0")
erro("10+10")
print("A aplicação foi finalizada.")