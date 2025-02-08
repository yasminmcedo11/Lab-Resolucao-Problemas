#Números Primos
n = int(input("Digite um número inteiro: "))
contador = 0
for i in range(1, n+1):
    if n % i == 0:
        contador += 1
if contador > 2:
    print("Não é primo!")
else:
    print("É primo!")            