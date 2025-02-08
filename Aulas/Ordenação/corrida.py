n, m = map(int, input().split())
lista_carros = []
for i in range(n):
    carro = list(map(int, input().split()))
    carro_individual = []
    carro_individual.append(i+1)
    carro_individual.append(sum(carro))
    lista_carros.append(carro_individual)
carros_ordenados = sorted(lista_carros, key = lambda linha: linha[1])
for i in range(3):
    print(carros_ordenados[i][0])


