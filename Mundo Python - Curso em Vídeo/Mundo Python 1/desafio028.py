#Jogo da Advinhação
import random

numero = int(input("Digite o número que você acha que foi sorteado, entre 0 e 5: "))
numero_escolhido = random.randint(0,5)
if numero == numero_escolhido:
    print("Você venceu")
else:
    print("Você perdeu")    