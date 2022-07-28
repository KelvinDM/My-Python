""""

Métodos Assessores-Getters e Setters.

São métodos utilizados na contrução
da interface Pública(Interface de Acesso)


Métodos Getters: sempre retornam valores

Get: Significa o retorno de dados

Métodos Setters: Sempre recebem valores
por parâmetros

Set: significa a atribuição de valor

Métodos aAcessores: Também garantem a integridade
das informações internas ao objeto


Exemplo:

get_+atributo
get_estudo()


set_atibuto
set_estudo()

get_idade() o valor será puxado.
set_idade(valor) é importante informar que o valor será atrubuido


"""




class Retangulo:

    def __init__(self,largura,altura):
        self.largura=0
        self.altura=0
        self.set_altura(altura)
        self.set_largura(largura)

    def set_altura(self,num):
        if(not(isinstance(num,int)and(num>0))):
            raise ValueError("Altura é invalida:{}".format(num))
        self.altura = num

    def set_largura(self,num):
        if (not (isinstance(num, int) and (num > 0))):
            raise ValueError("Largura é invalida:{}".format(num))
        self.largura = num
        
    def get_area(self):
        return  self.altura * self.largura



# r=Retangulo(largura=10,altura=5)
r=Retangulo(5,10)

print(r.get_area())








