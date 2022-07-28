"""
ENCAPSULAMENTO

É o isolamento do código.

Interface Pública é o conjunto de métodos
públicos para acessar os recursos e funcionalidades
do código encapsulado


Propriedades métodos

Interface Pública

Código


"""

class Retangulo:

    def __init__(self,largura,altura):
        self.l=largura
        self.a=altura

    def area(self):
        return  self.l * self.a

"""
Gerou erro informando varias vezes a palavra teste, poi o código
interno estava aguardando o rebimento de um valor do tipo inteiro
ou tipo float, ao receber uma string o mesmo tentou multiplicar
a palvara 5 vezes.

Por isso é necessario a interface :)
"""

r=Retangulo(10,5) #Gerou erro informando varias vezes a palavra teste
r.l="teste"
print(r.area())

