#Palpites para Mega Sena
import random

n_jogos = int(input("Digite o número de jogos que deseja criar: "))
lista_jogos = []
for i in range(n_jogos):
    linha = []
    for j in range(6):
        linha.append(random.randint(1, 60))
    lista_jogos.append(linha[:])
for posicao, jogo in enumerate(lista_jogos):
    print(f"Jogo {posicao+1}: {jogo}")
