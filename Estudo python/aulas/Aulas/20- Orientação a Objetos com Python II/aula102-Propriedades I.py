"""

PROPRIEDADES I

É um recurso para declaração de membros
públicos que permite invocar métodos
na leitura e escrita de valores

#escrita
instancia.attr=0
#leitura
x=instancia.attr

FUNÇÃO property()


property(fget,fset,fdel,doc)


"""


class A:
    def __init__(self):
        self._var = 0

    def _set_var(self,x):
        self._var=x
        print("Valor está sendo escrito")

    def _get_var(self):
        print("Valor está sendo lido")
        return self._var

    var=property(fget=_get_var, fset=_set_var)


a=A()
a.var=10
print(a.var)


