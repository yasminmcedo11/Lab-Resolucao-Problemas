#Seno, Cosseno e Tangente
import math

n = float(input("Digite o valor do ângulo: "))
sen = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tg = math.tan(math.radians(n))
print("Os valores de seno, cosseno e tangente são {:.2f}, {:.2f} e {:.2f}.".format(sen, cos, tg))