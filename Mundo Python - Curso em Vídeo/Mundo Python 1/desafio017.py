#Catetos e Hipotenusa
import math

ca = float(input("Digite o valor do cateto adjacente: "))
co = float(input("Digite o valor do cateto oposto: "))
hipotenusa = math.sqrt(math.pow(ca, 2) + math.pow(co, 2))
print("O valor da hipotenusa é {:.2f}.".format(hipotenusa))