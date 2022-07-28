"""


INSTRUÇÃO BREAK

É a instrução que interrompe a execução do laço de
repetição na queal está contida


"""

"""
for top in range(10):
    if (True):
        break



i=10
while (i<100):
    i=i+1
    if(True):
        break
        
"""

print("Antes de entrar no Laço de repetição")

for item in range(10):
    print(item)
    if(item==6):
        #print("A condição estabelecida retornou um valor verdadeiro")
        break
print("Depois de ter entrado no laço de repetição")