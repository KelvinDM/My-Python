"""
18) Faça um algoritmo que valide uma data. A mesma deve
ser formada por dia, mês e ano. Por exemplo, se o usuário digitar a data 10/8 a mesma será inválida.
Porém, caso a data seja 01/10/2018, a mesma deve ser considerada válida.
"""

"""
print(' ##### DATA #####\n')
data = input('Digite uma data no formato dd/mm/aaaa: ')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])



if len(data) == 10:
if (0 < ano < 10000):
if (0 < mes <= 12):
if (mes == 2 and (ano % 4) == 0):
if 0 < dia <= 29:
print('Esta é uma data válida.')
else:
print('Esta não é uma data válida.')
elif mes == 2 and (ano % 4) != 0:
if 0 < dia <= 28:
print('Esta é uma data válida.')
else:
print('Esta não é uma data válida.')
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
if 0 < dia <= 30:
print('Esta é uma data válida.')
else:
print('Esta não é uma data válida.')
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
if 0 < dia <= 31:
print('Esta é uma data válida.')
else:
print('Esta não é uma data válida.')
else:
print('Esta não é uma data válida.')
else:
print('Esta não é uma data válida.')
else:
print('Esta não é uma data válida.')
else:
print('Esta não é uma data válida.')

"""

data = input("Digite um data com o formato dd/mm/aaaa :")

dia, mes, ano = map(int, data.split('/'))

valida = False

# Meses com 31 dias
if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or
mes == 8 or mes == 10 or mes == 12):
 if (dia <= 31):
        valida = True

# Meses com 30 dias
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if (dia <= 30):
        valida = True

#se o mês for fevereiro, precisamos saber se ele é Bissexto
if (mes == 2):

 if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    if (dia <= 29):
        valida = True
elif (dia <= 28):
        valida = True


if (valida):
    print('Data válida')
else:
    print('Inválida')