"""

ITERANDO STRINGS

O PROCESSO  FUNCIONA DA MESMA FORMA QUE A ITERAÇÃO
DE QUALQUER OUTRA LISTA DE OBJETOS

"""
#EXEMPLO1
# s= 'Iterando Strings'
#
# for c in s:
#     print(c)


#EXEMPLO2

# s= 'Iterando Strings'
# indice=0
#
# while indice< len(s):
#     print(indice, s[indice])
#     indice=indice+1

#EXEMPLO 3

for k,v in enumerate('Iterando Strings'):
    print(k, v)
#enumerate serve para vincular uma lista de números
#inteiros a determinados valores associados a variavel



