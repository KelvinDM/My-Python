"""

Orientação a Objetos:
OBEJETO CLASSE

As CLASSES são utilizadas para criar objetos
e em Python as mesmas também são objetos


MEMBRO DE CLASSE

MEMBRO DE INSTÂNCIA


OBJETO CLASSE
Todo membro definido no objeto classe
pode ser acessado de qualquer instância que foi
 gerado dessa classe

INSTÂNCIA DE CLASSE
o membro declarado na instância de classe não
estara disponivel no objeto classe.


OBJETO CLASSE
Há diversos benefícios na utilização da
CLASSE OBJETO mas que, talvez, não seja muito
fácil reconhecê-los num primeiro momento


"""


class MinhaClasse:
    pass


obj=MinhaClasse()

print(type(obj))

print(type(MinhaClasse))

print(50*'-')


print(obj.__class__)
print(MinhaClasse.__class__)


print(50*'-')



# print(obj.__name__)
print(MinhaClasse.__name__)
print(obj.__class__.__name__)


print(50*'-')


MinhaClasse.var_cls=0
print(MinhaClasse)
# print(MinhaClasse.__dict__)

from pprint import  pprint
pprint(MinhaClasse.__dict__)


pprint(obj.__dict__)

print(obj.var_cls)
MinhaClasse.var_cls=10
print(obj.var_cls)






