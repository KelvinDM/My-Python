"""


EXCEÇÕES

BLOCO ELSE

"""

def erro(x):
    try:
        eval(x)
    except ValueError as e:
        print(type(e))
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except (TypeError,NameError) as e:
        print(type(e))
    else:
        print("Nenhuma exceção ocorreu")
#caso nenhuma exceção for levantada a função
#else será executada




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