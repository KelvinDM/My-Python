"""

PARÂMETROS DEFAULT

É um parâmetro inicializado com valor default

"""

#VEJA QUE AQUI INFORMEI 3 VARIAVEIS RECEBENDO OS VALORES
#E DEPOIS INVOQUEI CADA UMA DELAS
def login(sistema="Windows",usuario="root",senha="123"):
    print("Sistema Operacional:",sistema)
    print("Usuário:",usuario)
    print("Senha:",senha)

print(10*"-","Padrão Normal!!!",10*"-")
login()
print(50*"-")
login("Linux","Kelvin",78459632)


