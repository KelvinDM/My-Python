"""

INTRODUÇÃO AOS DICIONÁRIOS

É um tipo de lista não ordenada na qual cada
elemento está associado a uma chave.



"""
#EXEMPLOS DA HORA

d1={}

print(type(d1))

d2=dict()

print(type(d2))

d1['aaa']=1000
d1['bbb']=2000
d1['ccc']=3000

print(d1)

print(d1['bbb']) #Como o 2000 ficou associado a strinf bbb
#ele demonstrou esse valor

d2={1.1:"teste1",2.2:"teste2",3:"teste3"}

print(d2)
print(d2[1.1])
print(d2[2.2])


