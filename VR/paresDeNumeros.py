#100% certo
from itertools import combinations

n, inicio, fim = map(int, input().split())
lista = list(map(int, input().split()))
numeros = 0
lista_combinada = list(combinations(lista, 2))
for i in range(len(lista_combinada)):
    if inicio <= sum(lista_combinada[i]) <= fim:
        numeros += 1
print(numeros)