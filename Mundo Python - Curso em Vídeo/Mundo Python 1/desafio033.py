#Maior e Menor valores
numeros = list(map(int, input("Digite os 3 números: ").split()))
maior = max(numeros)
menor = min(numeros)
print("O maior número é {} e o menor número é {}.".format(maior, menor))