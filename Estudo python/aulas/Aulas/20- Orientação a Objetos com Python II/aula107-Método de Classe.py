"""


Método de Classe

É um método que receberá a instância da
classe como primeiro argumento


"""

"""
#EXEMPLO

class A:
    def func(cls,arg1,arg2):
        pass
    classmethod(func)


class B:
    @classmethod
    def func(cls,ar1,ar2):
        pass
"""

class Bichos:
    quant_bichos=0
    def __init__(self):
        self.add_bicho()
    def __del__(self):
        self.del_bicho()
        if(self.quant_bichos==0):
            print("Todos os bichos foram mortos!!")
    @classmethod
    def add_bicho(cls):
        cls.quant_bichos +=1
    @classmethod
    def del_bicho(cls):
        cls.quant_bichos-=1

    # add_bicho=classmethod(add_bicho)
    # del_bicho=classmethod(del_bicho)

b1=Bichos()
print(Bichos.quant_bichos)
b2=Bichos()
print(Bichos.quant_bichos)
b3=Bichos()
print(Bichos.quant_bichos)

del (b1)
print(Bichos.quant_bichos)
del (b2)
print(Bichos.quant_bichos)
del (b3)
print(Bichos.quant_bichos)