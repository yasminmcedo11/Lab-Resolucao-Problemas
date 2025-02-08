#Maior e Menor Valores na Lista
numeros = list(map(int, input("Digite 5 números: ").split()))
maior = max(numeros)
menor = min(numeros)
for posicao, numero in enumerate(numeros):
    if numero == maior:
        indice_maior = posicao
    if numero == menor:
        indice_menor = posicao
print(f"O maior valor foi de {maior}, posição {indice_maior}. O menor valor foi de {menor}, na posição {indice_menor}")

