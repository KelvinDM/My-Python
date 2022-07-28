"""

 l.append('eee')
l
['bbb', 'ccc', 'ddd', 'eee']
 l.insert(0,'aaa')
 l
['aaa', 'bbb', 'ccc', 'ddd', 'eee']
l[1]
'bbb'
 l[1] ='bbbb'
 l
['aaa', 'bbbb', 'ccc', 'ddd', 'eee']
 l.clear()
 l=['aaa', 'bbbb', 'ccc', 'ddd', 'eee']
 l
['aaa', 'bbbb', 'ccc', 'ddd', 'eee']
 l.pop()
'eee'

 l
['aaa', 'bbbb', 'ccc', 'ddd']
l.pop(0)
'aaa'
l
['bbbb', 'ccc', 'ddd']
 l.pop(-1)
'ddd'
 l
['bbbb', 'ccc']
 l=['aaa', 'bbbb', 'ccc', 'ddd', 'eee']
 l
['aaa', 'bbbb', 'ccc', 'ddd', 'eee']
 del(l[2:4])
 l
['aaa', 'bbbb', 'eee']
 l=['aaa', 'bbbb', 'ccc', 'ddd', 'eee']
> l
['aaa', 'bbbb', 'ccc', 'ddd', 'eee']
 del(l[::2])
> l
['bbbb', 'ddd']


"""


# VEJA ABAIXO ALGUNS MÉTODOS DE INSERÇÃO EMODIFICAÇÃO DA LSITA
l=['aaa','bbb','ccc']

print(l)

l.insert(0,'abc')
l.insert(0,'teste')
print(l)

#l.clear() SERVE PARA LIMPAR A LISTA
#print(l)

l.pop(0)
print(l)

l.pop(-1)
print(l)


del(l[0:1]) # A EXCLUSÃO DE LOCAIS NA LISTA CONTA A PARTIR DA LEITURA 0

print(l)