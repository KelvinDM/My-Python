"""
Exceções
Tratamento de Múltipla exceções


"""


def erro(x):
    try:
        eval(x)
    except TypeError:
        print("TypeError")
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