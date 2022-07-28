"""

ARGUMENTOS

POSICIONAIS X NOMEADOS


"""

def dados_pessoais(nome,sobrenome,idade,sexo):
    print("Nome:{}\nSobrenome: {}\nIdade: {}\nSexo: {}"
          .format(nome,sobrenome,idade,sexo))


#Argumentos Posicionais
dados_pessoais("Cláudio","Rogério",30,True)

print(50*"-")

#Argumentos NOMEADOS
dados_pessoais(idade=30,
               sexo=True,
               sobrenome="Carvalho",
               nome="Cláudio")
#MESMO INFORMANDO O LOCAL DIFERENTE DOS VALORES DAS VARIAVEIS
#O DICIONARIO AINDA IRA MOSTRAR NA POSIÇÃO INFORMADA INICIALMENTE


