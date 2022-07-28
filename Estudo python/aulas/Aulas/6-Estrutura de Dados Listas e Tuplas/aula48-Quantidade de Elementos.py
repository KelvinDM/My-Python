


#QUANTIDADE DE ELEMENTOS

lista= ['Cláudio','José','Maria','Beltrano','João','Fulano','Ciclano',]
print(lista)



#len(lista)  UTILIZADO PARA VERIFICAR A QUANTIDADE DE ELEMENTOS NA LISTA
print(len(lista))


print(lista[-1])

lista.insert(5,'José')
lista.insert(0,'José')
lista.insert(3,'José')

lista.append('José')
print(lista)


#lista.count('José') .count  Serve par amostrar quantas vezes um elemento aparece dentro da lista
print(lista.count('José'))


print('Maria aparece:',lista.count('Maria'))

#lista.index('Maria') .index  Serve para mostrar em qual posição está determiando elemento dentro da lista
print('Posição do Elemento Maria:',lista.index('Maria'))

print('Posição do Elemento José:',lista.index('José'))

