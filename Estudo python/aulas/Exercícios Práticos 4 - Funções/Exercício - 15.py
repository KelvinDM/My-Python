"""

15) Escreva uma função que verifique se um número está num intervalo determinado.


"""

num1=int(input("Informe o número para verificar o intervalo:"))

def intervalo(a,b):
    if (num1>=a) and (num1<=b):
        print("O número informado está dentro do intervalo do número",a,"e",b)
    else:
        print("O número não está dentro do intervalo")

intervalo(10,50)
