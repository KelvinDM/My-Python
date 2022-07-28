"""

Faça um algoritmo que solicite a nota das
4 provas semestrais do usuário. Em seguida,
 calcule e envie para a saída padrão a média:



"""

nota1=float(input("Informe a nota do primeiro semestre:"))
nota2=float(input("Informe a nota do segundo semestre:"))
nota3=float(input("Informe a nota do terceiro semestre:"))
nota4=float(input("Informe a nota do quarto semestre:"))


soma=nota1+nota2+nota3+nota4
media=soma / 4

print("Média do aluno:%.1f"%media)