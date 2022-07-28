




s="Lista de Caracteres"

print(s)

print(len(s))
print(len("a"))

print(s.split(" "))
#SPLIT serve para separar as strings a partir de um caractere de separação
lista=s.split(" ")

print(lista[0]+' '+lista[2])

s=s.replace("Lista","Amor") #REPLACE serve para trocar uma string por outra
s=s.replace("Caracteres","Python")
s=s.replace("de","por")
print(s)
