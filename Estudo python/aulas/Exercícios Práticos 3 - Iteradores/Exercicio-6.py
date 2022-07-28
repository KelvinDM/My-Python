"""


6) Faça um algoritmo que imprima os números primos entre 0 e 100:
"""

"""
x=0
for list in range (1,100,1):
    if (list%2==1):
        print(list)
        if (True):
            x=x+1

print("A quantidade de números pares entre 0 e 100 é: %i" %(x))


"""
tot=0
start = 1
end = 100

for list in range(start, end + 1):
    if list > 1:
        for x in range(2, list):
            if (list % x == 0):
                if (False):
                    tot = tot + 1

                break
        else:

            print(list)

