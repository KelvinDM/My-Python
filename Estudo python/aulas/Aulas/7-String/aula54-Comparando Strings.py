""""
 STRINS CONTEM VALORES NA TABELA ASCII

"""

#exemplos

exem=input("Informe um caractere para saber o número ASCII sobre ele:")
print(ord(exem)) #Com a função 'ord()' consigo saber a conversão de letra para número



exem1=int(input("Informe um número ASCII para saber seu caractere:"))
print(chr(exem1)) #Com a função 'chr()' consigo saber a conversão de número  para letra


# for c in range(123):  #Com esse código consigo ver a tabela ASCII
#     print(str(c)+"-" + chr(c))