
num1 = int(input("Digite um número:"))
num2 = int(input("Digite o segundo número:"))
num3 = 5,2


if(num1==num2):
    print("O primeiro número %d é igual ao segundo número %d" %(num1,num2))


if(num1>10):
    print("O valor é maior do que 10!")
    if(num1<=15):
        print("O valor é maior doque 10 mas menor do que 15")
    else:
        if(num1<=50):
            print("O valor é maior do que 10, mas menor do que 50.")
        else:
            print("O valor é maior do que 50.")

else:
    if(num1>5):
        print("O número é menor do que 10 mais é maior do que 5!")
        if(num1==7):
            print("O número é igual a 7!")
        if(num1==8):
            print("O número é igual a 8.")

    else:
        if (num1 >= 1):
            print("O número é maior ou igual a 1.")
        else:
            print("O valor é menor do que 5.")

if(num1>=100):
    print("O valor é maior ou igual a 100.")
else:
    print("O valor é menor do que 100.")

