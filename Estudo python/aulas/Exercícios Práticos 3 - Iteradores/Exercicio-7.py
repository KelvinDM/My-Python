"""
7) Faça um algoritmo que calcule os número primos num intervalo pré-determinado pelo usuário:


"""
print("INFORME ABAIXO O INTERVALO EM QUE SERÁ DETERMICADO A CONTAGEM DOS NÚMEROS PRIMOS!!")
print()


start=int(input("Número inicial:"))
end=int(input("Número final:"))

if (start>end):
    print("Informe o intervalo corretamente!!")

tot=0

for list in range(start, end + 1):
    if list > 1:
        for x in range(2, list):
            if (list % x == 0):


                break
        else:

            print(list)
            if(True):
                tot=tot+1



print("Total de números primos entre %i e %i é %i " %(start,end,tot))