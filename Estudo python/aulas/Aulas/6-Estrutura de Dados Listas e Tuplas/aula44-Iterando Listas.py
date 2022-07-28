#ITERANDO LISTAS EM PYTHON


listanum=[100,200,300,400]

for item in listanum:
    print(item)



listanum=[100,200,300,400,500,600]
listaindice=range(4)

for item in listaindice:
    listanum[item]+=1000
print(listanum)



listanum=[100,200,300,400,500,600,700,800]

for item in range(len(listanum)):
    listanum[item]+=1000
print(listanum)




listanum=[100,200,300,400,500,600,700,800]

for idx, item in enumerate(listanum):
    listanum[idx]+=1000
print(listanum)
