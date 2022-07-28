"""

ANÁLISE DA DECLARAÇÃO DE MEMBROS


MEMBROS: Podem ser adicionados a objetos
de forma interna ou externa a classe

"""


class Retangulo:

    def area(self):
        return  self.a * self.l #Return é utilizado apenas em FUNÇÕES


def membros_retangulo(r):
    r.a=0
    r.l=0


r1=Retangulo()
membros_retangulo(r1)
r1.l=10
r1.a=5

print(r1.area())
print(r1.area())