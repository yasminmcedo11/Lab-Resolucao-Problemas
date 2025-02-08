#Funções para Sortear e Somar
import random

def sorteia(lista):
    for i in range(5):
        lista.append(random.randint(1, 10))
    
def soma_pares(lista):
    soma = 0
    for numero in lista:
        if numero % 2 == 0:
            soma += numero
    return soma

numeros = []
sorteia(numeros)
soma = soma_pares(numeros)
print(f"A lista foi formada pelos números {numeros}")
print(f"A soma dos pares foi de {soma}")