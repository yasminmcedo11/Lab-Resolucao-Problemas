#Jogo de Advinhação v2.0
import random

numero = int(input("Digite o número que você acha que foi sorteado, entre 0 e 10: "))
numero_escolhido = random.randint(0,10)
contador = 0
while numero_escolhido != numero:
    numero = int(input("Digite o número que você acha que foi sorteado, entre 0 e 10: "))
    contador += 1
print("Você levou {} vez(es) para acertar o número sorteado.".format(contador))  