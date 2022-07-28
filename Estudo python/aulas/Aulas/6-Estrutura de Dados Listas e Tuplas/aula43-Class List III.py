"""
lista=[1,2,3,4,5]
lista
[1, 2, 3, 4, 5]
lista= lista +[6]
 lista
[1, 2, 3, 4, 5, 6]
lista= [0] + lista
lista
[0, 1, 2, 3, 4, 5, 6]
lista= lista +[7,8,9,10]
lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista = lista +8
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    lista = lista +8
TypeError: can only concatenate list (not "int") to list
lista.append(11)
lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
lista.append([11])
lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, [11]]
del(lista[-1])
lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
10*[0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
lista +=10*[0]
lista
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
50*"-"

"""


print("SEJA BEM VINDO AS LISTAS :D ")

list1=[16,17,18,19,20]

# print(100*"-")
#
lista=[1,2,3,4,5]
#
# print(lista)
#
# lista=[0]+lista
# print(lista)
#
# lista=1*[0]+lista
# print(lista)
#
# lista=lista+[8,9,10,11,12,13,14,15]
# print(lista)

lista.append(list1)
print(lista)

# del(lista[0])
# print(lista)
#
# del(lista[-1])
# print(lista)
#
# lista=lista+list1
# print(lista)
#
# lista=10*[1]
# print(lista)