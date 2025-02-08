#Maior e Menor Valores em Tuplas
import random

x = []
for i in range(5):
    n = random.randint(0, 100)
    x.append(n)
y = tuple(x)
print(f"Os números gerados foram: \n{y}")
for i in range(len(y)):
    if i == 0:
        maior = y[0]
        menor = y[0]
    if y[i] > maior:
        maior = y[i]
    if y[i] < menor:
        menor = y[i]    
print(f"O menor valor gerado foi de {menor}, já o maior valor gerado foi de {maior}.")
    

