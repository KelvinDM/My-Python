num_int = 5
num_dec = 7.3
val_str = "qualquer texto"


"""
%i = Numero inteiro
%f = Numero flutuante(float)
%s = Numero String

"""



print("O valor é:",num_int)
print("O valor é: %i" %num_int)
print("O valor é: " + str(num_int))

print ("Concatenando decimal:", num_dec)
print ("Concatenando decimal: %.10f" %num_dec) #Variaveis do tipo FLOAT devemos controlar as casas decimais utilizando %.10f dentro da STRING (NÃO ESQUEÇA)
print ("Concatenando decimal: " + str(num_dec))




print("Concatenando Strings:" ,val_str)
print("Concatenando Strings: %s" %val_str)
print("Concatenando Strings: " + val_str)