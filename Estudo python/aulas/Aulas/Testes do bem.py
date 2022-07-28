"""x = 10
if(x > 10):
    print("bloco de instrução True")
else:
    print("bloco de instrução False")


x = 10

if(x > 10):
    print("Bloco de instrucao True")
else:
    print("Bloco de instrucao False")
    

"""

# print("Vamos cadastrar sua conta,digite abaixo seu login e senha!!")
# log=input("Informe seu login:")
# sen=input("Informe sua senha:")
# print()
# print("CONTA CADASTRADA COM SUCESSO!!!")
#
#
# print()
#
# login=input("Informe seu LOGIN:")
# senha=input("Informe sua SENHA:")
#
#
# while login != log: #REPETIR O CÓDIGO ATÉ QUE SEJA CONFIRMADA A SENHA CORRETA
#     print('LOGIN OU SENHA INCORRETOS!!')
#     print()
#     login = input('Informe seu LOGIN:')
#     senha = input("Informe sua SENHA:")
#
#
# while senha != sen: #REPETIR O CÓDIGO ATÉ QUE SEJA CONFIRMADA A SENHA CORRETA
#     print('SENHA INCORRETA!!')
#     print()
#     senha = input('Informe sua SENHA:')


# from kivy.app import App
#
# from kivy.uix.label import Label
#
# def build():
#     return Label(text="Hello World")
#
# oi=App()
# oi.build=build
# oi.run()

"""
class Guerreiro():
    #CARACTERISTICAS DO GUERREIRO
    def __init__(self,cabelocor,corpo,armadura,arma):
        self.cabelocor=cabelocor
        self.corpo=corpo
        self.armadura=armadura
        self.arma=arma

    # MÉTODOS DO GUERREIRO
    def lutar(self,botao):
        if botao == 'q':
            print("Atacar")
        if botao == 'e':
            print("Defender")

    # atacar
    # esquivar
    # defender
    # andar

#GUERREIRO
guerreiro_bom=Guerreiro("vermelho","magro","armadura de prata","machado")
print(guerreiro_bom.cabelocor)
guerreiro_bom.lutar('q')

#GUERREIRO 2
guerreiro_bom2=Guerreiro("vermelho","magro","armadura de prata","machado")
guerreiro_bom2.lutar("e")
"""

#EXEMPLO SITE NETFLIX

class Cliente:
    def __init__(self,nome,email,plano):
        self.nome=nome
        self.email=email
        self.lista_planos=["basic","premium"]
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido!!")


    def mudar_plano(self,novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("Plano Inválido")


    def ver_filme(self,filme,plano_filme):
        if self.plano == plano_filme:
            print(f"Ver filme {filme} ")
        elif self.plano == "premium":
            print(f"Ver filme {filme} ")
        elif self.plano == "basic" and plano_filme == "premium":
            print("Faça upgrade para premium para ver esse filme.")
        else:
            print("Plano invalido")



cliente=Cliente("kelvin","kelvindaniel1932@gmail.com","basic")
print(cliente.plano)
cliente.ver_filme("Harry Potter","premium")

#botao de upgrade
cliente.mudar_plano("premium")
print(cliente.plano)
cliente.ver_filme("Harry Potter","premium")

