"""

PERSONALIZANDO O MÉTODO CONSTRUDO

Term a finalizad de estabelecer os valores
obrigatórios para construção do novo objeto


"""

class A:
    def __init__(self,x,y):
        pass


class Retangulo:

    def __init__(self,largura,altura):
        self.l=largura
        self.a=altura


    def area(self):
        return self.l * self.a

r=Retangulo(2,5)
print(r.area())
