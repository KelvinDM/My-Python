print(' ##### DATA #####\n')
data = input('Digite uma data no formato dd/mm/aaaa: ')

is_valid = True
data_split = data.split('/')

if len(data_split) <= 3:
    is_valid = False

if is_valid and (len(data_split[0]) != 2 or len(data_split[1]) != 2 or len(data_split[2]) != 4):
    is_valid = False

dia = 0
mes = 0
ano = 0
try:
    dia, mes, ano = map(int, data_split)
except:
    is_valid = False 

if ano < 0 or dia < 1 or mes < 1:
   is_valid = False 

if dia == 31 and mes not in [1, 3, 5, 7, 8, 10, 12]: 
   is_valid = False 
elif dia == 30 and mes not in [4, 6, 9, 11]:
   is_valid = False 
elif dia == 28 and mes != 2:
   is_valid = False 
elif is_valid and (dia == 29 and mes == 2):
    ano_post = data_split[2][-2]

    if ano_post != '00':
        is_valid = ano % 4 == 0    
    else:
        is_valid = ano % 400 == 0

if is_valid:
    print('Esta é uma data válida.')  
else:
    print('Esta não é uma data válida.')