#Dividindo Valores em Várias Listas
numeros = list(map(int, input("Digite os números que desejar: ").split()))
pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f"A lista inicial: {numeros} \nLista de pares: {pares} \nLista de ímpares: {impares}")    