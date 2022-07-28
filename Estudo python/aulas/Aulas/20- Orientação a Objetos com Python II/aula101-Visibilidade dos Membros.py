"""

Visibilida dos Membros:
É um recurso da orientação a objetos
que impede o acesso externo a membros de uso
exclusivamente interno ao objeto

A ocultação de membros não ocorre na prática
o Python não possui este recurso


MEMBROS DE USO INTERNO:
Membros de uso eclusivamente interno
ao objeto deverão ter seus nomes
preceditos por UM underline

publico=0
_restrito=0


exemplo:

class Pessoa:
    def__init__(self):
    self._attr=0
    def _func(self):
    pass

"""

"""

COLISÃO DE NOMES
Para evitar a colisão de nomes entre a
superclasse e a subclasse o membro deve ser
precedido por DOIS underlines

Ex:
__colisao=0

class Pessoa:
def __init__(self):
self.__attr=0

MÉTODOS MÁGICOS:
São preceidos e dinalizados
com DOIS underlines(dunders) e são
eclusivos da linguagem
ex:

__linguagem__=""
    def__init__(self):
    pass


"""




class Retangulo:

    def __init__(self, largura, altura):
        self._largura = 0
        self._altura = 0
        self.__var= 0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self, num):
        if (not (isinstance(num, int) and (num > 0))):
            raise ValueError("Altura é invalida:{}".format(num))
        self._altura = num
        self.__var=456

    def set_largura(self, num):
        if (not (isinstance(num, int) and (num > 0))):
            raise ValueError("Largura é invalida:{}".format(num))
        self._largura = num

    def get_area(self):
        return self._altura * self._largura


# r=Retangulo(largura=10,altura=5)
r = Retangulo(5,5)
r = Retangulo(5,5)



print(r.get_area())
