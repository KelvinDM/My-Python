"""

MÓDULOS

Importação de módulos: Copia atributos de um
módulo diretamente á tabela de símbolos local


from modulo import simb1,simb2

IMPORTAÇÃO DE SÍBOLOS RENOMEÇÃO

import modulo as M

from modulo import simbolo as s

as= significa como

------------------------------------
from modulo impot simbolo

MESMA COISA

import modulo
simbolo= modulo.simbolo
----------------------



IMPORTAÇÃO DE SÍBOLOS

from modulo import*
importa todos os simbolos do determinado módulo
não é aconselhavel fazer isso
"""


from math import * #importei todos os simbolos do módulo

# from math import pi,e

# import math
# e=math.e
# pi=math.pi

def func():
    from math import factorial
    print("O factorial de 10 é:",factorial(10))# Importei simbolo para saber o factorial de 10

func()


from math import sqrt #square=raiz quadrada

print("A raiz quadrada de 9 é:",sqrt(9))
print("Valor de PI:",pi)
print("Valor de e:",e)


