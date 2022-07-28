"""A atribuição condicional é uma estrtura utilizada para  simplificar o código
cujo o valor a ser atribuido será aquele que satisfazer a condição"""


#teste = 10 if (True) else 20

"""
>>> texto= "sim" if x==10 else "não"
>>> texto
'sim'
>>> texto
'sim'
>>> x=9
>>> texto= "sim" if x==10 else "não"
>>> texto
'não'
"""


num1 = int(input("Digite um número: "))
s = "par" if num1 % 2==0  else "impar"

print(f"O número digitado é {s}")