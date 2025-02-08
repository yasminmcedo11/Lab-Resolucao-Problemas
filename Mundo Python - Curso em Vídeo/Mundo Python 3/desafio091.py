#Jogos de Dados em Python
import random

jogadores = []
resultado = {}
for i in range(4):
    resultado["Nome"] = f"Jogador {i+1}"
    resultado["Número"] = random.randint(1,6)
    print(f'O {resultado["Nome"]} tirou {resultado["Número"]}')
    jogadores.append(resultado.copy())
for i in range(len(jogadores)):
    for j in range(i+1, len(jogadores)):
        if jogadores[i]["Número"] > jogadores[j]["Número"]:
            jogadores[i], jogadores[j] = jogadores[j], jogadores[i]
print(jogadores)  