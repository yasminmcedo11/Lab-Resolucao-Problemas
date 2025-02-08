#20% de erro
import math

a, b, c, d = map(int, input().split())
def calcular_mmc (a, b):
    return abs(a*b)// math.gcd(a, b)
if b == d:
    numero = a + c
    if numero % b == 0:
        divisor = 1
        dividendo = numero/b
        print(int(dividendo), divisor)
else:
    divisor = calcular_mmc(b, d)
    a = (divisor/b)*a
    c = (divisor/d)*c
    dividendo = a + c
    if dividendo % divisor == 0:
        numero = dividendo/divisor
        print(int(numero), int(1))
    else:
        print(int(dividendo), int(divisor)) 