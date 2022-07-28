"""

18) Escreva uma função capaz de receber uma quantidade indeterminada de parâmetros e
imprima na telas os números primos contidos nessa lista.


"""


tot=0
start = 1
end = 100
lista=0
def func():
    for list in range(start, end + 1):
        if list > 1:
            for x in range(2, list):
                if (list % x == 0):
                    if (True):
                        pass

                    break
            else:

                print(list)


func()

