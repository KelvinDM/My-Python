"""

9) Faça um algoritmo que imprima a frase "estou em looping" e, em seguida,
solicite ao usuário digitar uma letra. Caso a letra seja o "q" finalize a aplicação.
 Do contrário, imprima novamente a mesma frase até que o caractere "q" seja enviado:

"""
a='a'
while a != 'q': #REPETIR A FRASE ATÉ QUE SEJA CONFIRMADA A LETRA DIGITADA
    print('estou em loop')
    a = input('Digite uma letra: ')