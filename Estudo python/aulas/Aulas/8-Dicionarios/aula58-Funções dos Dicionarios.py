

tel={}
tel={}
tel={30301122:"Pericles",
     33547877:"Menelau",
     33381245:"Atreu",
     36458899:"Tieste"}

print(tel)

print(len(tel))

del(tel[36458899])

print(tel)

print(tel.keys()) #KEYS é utilizado para retornar o valor de chave associado da minha variavel
print(tel.values())#VALUES é utilizado para retornar o valor da variavel associada a chave

print(tel[30301122]) # Veja dois exeplos de como puxar o valor de uma chave

print(tel.get(30301122))

#------------------------------------------------------------------------------------------------------------------
tel={}
tel={}
tel={30301122:"Pericles",
     33547877:"Menelau",
     33381245:"Atreu",
     36458899:"Tieste"}

print(tel)

print(tel.popitem())# POPITEM aparece o valor de uma lista e depois remove
print(tel)
print(tel.popitem())
print(tel)
print(tel.popitem())
print(tel)

#-----------------------------------------------------------------------------------------------------------------

tel={}
tel={}
tel={30301122:"Pericles",
     33547877:"Menelau",
     33381245:"Atreu",
     36458899:"Tieste"}

print(36458899 in tel)

print(362458899 in tel)

tel2={999999999:"teste1",55551111:"teste2"}

print(tel2)

tel.update(tel2)# .update utilizado para mesclar os elementros de dois dicionarios.
print(tel)

t=(10,10,10)
tel[t] ="eXcript"
print(tel)

l=[1,2,3]
tel[l]=55
print(tel) #não ira funcionar pois não podemos adicionar uma lista como chave de um valor

