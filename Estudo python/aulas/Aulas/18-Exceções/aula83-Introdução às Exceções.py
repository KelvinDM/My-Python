"""

Exceções

Exceção é todo o desvio da regra geral
(Dicionário Aurélio)

Tratamento de Exceção:
É todo código que identifica
erros e implmenta uma solução
evitando que a aplicação seja
finalizada


Levantamento de Exceção:
É todo código que ao perceber um
problema cria uma exceção avisando
o programador


try: função utilizada para iniciar uma exceção
except ErroClass:


#Exemplo

try:
    codigo
except ErroClass1:
    tratamento
except ErroClass2:
    tratamento

Traceback
"""

try:
    a=10/0
    print(a)
except ZeroDivisionError:
    print("Não é possivel dividir um número por zero.")