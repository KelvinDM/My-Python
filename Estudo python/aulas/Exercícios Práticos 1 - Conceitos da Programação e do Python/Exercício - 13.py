"""

Faça um algoritmo que solicite ao usuário informar uma quantidade

de dias, horas, minutos e segundos.

Em seguida, converta tudo para segundos:



"""

dia=int(input("Informe a quantidade de dias:"))
hor=int(input("Informe a quantidade de horas:"))
min=int(input("Informe a quantidade de minutos:"))
sec=int(input("Informe a quantidade de segundos:"))


resultdia=dia*86400
resulthor=hor*3600
resultmin=min*60

totalsec=resultdia+resulthor+resultmin+sec

print()
print("%s dias é equivalente á: %s segundos"%(dia,resultdia))
print()
print("%s horas é equivalente á: %s segundos"%(hor,resulthor))
print()
print("%s minutos é equivalente á: %s segundos"%(min,resultmin))
print()
print("A quantidade de segundos informado é: %s"%sec)
print()
print("A soma total em segundos é equivalente á:%s"%totalsec)