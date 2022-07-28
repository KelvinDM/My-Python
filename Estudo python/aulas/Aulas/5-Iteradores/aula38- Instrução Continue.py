"""

INTRUÇÃO CONTINUE

É a instrução que interrompe a execução de apenas
um único ciclo


"""


print()
print("Inicio")

i=0
while(i<10):
    i=i+1
    if(i%2==0):
        continue
    if (i>5):
        break
    print(i)
else:
    print("Else")
print("Fim")
print()