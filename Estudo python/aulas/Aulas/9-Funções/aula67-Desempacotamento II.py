



lista=[11,10,12]
tupla=11,10,12

def func(a,b,c):
    print(a)
    print(b)
    print(c)

lista.sort()
func(*lista)

# l=[*tupla]#serve para coverter o tipo tupla para tipo lista
# l.sort()#.sort serve para ordenar a lista
# func(*l)

# func(**dict(zip(("b","a","c"),lista)))