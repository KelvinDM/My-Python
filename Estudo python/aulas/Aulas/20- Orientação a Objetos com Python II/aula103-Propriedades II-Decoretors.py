"""

PROPRIEDADES

DECORATORS

O decorador de Método adiciona funcionalidades
ao método sem alterar a sua implementação


class A:
    def__init__(self):
    self._x=0
    def get_x(self):
    return self._x
    x=property(fget=get_x)


"""

# class A:
#     def __init__(self):
#         self._x=0
#     @property
#     def x(self):
#         return  self._x
#     @x.setter  #@x=propriedade  setter=ação
#     def x(self,val):
#         self._x=val

class A:
    def __init__(self):
        self._var = 0

    @property
    def var(self):
        print("Valor está sendo lido")
        return self._var

    @var.setter
    def var(self,x):
        print("Valor está sendo escrito")
        self._var = x


    # var=property(fget=_get_var, fset=_set_var)


a=A()
a.var=10
t=a.var
print(t)









