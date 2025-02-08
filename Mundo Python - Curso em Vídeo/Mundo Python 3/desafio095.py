#Aprimorando Dicionários
jogador = {}
jogadores = []
gols_total = 0
gols_partida = []
while True:
    jogador["Nome"] = input("Digite o nome do jogador: ")
    jogador["Partidas Jogadas"] = int(input("Digite a quantidade de partidas jogadas: "))
    numero = jogador["Partidas Jogadas"]
    for i in range(numero):
        gols = int(input(f"Digite a quantidade de gols feitos na partida {i+1}: "))
        gols_partida.append(gols)
        gols_total += gols
    jogador["Gols Feitos"] = gols_total
    jogadores.append(jogador.copy())
    r = input("Deseja continuar? [N\S]").strip()[0]
    if r not in "Ss":
        break
for jogador in jogadores:
    for pos, valor in jogador.items():
        print(f"{pos}: {valor}")
jogador_detalhes = int(input("Deseja ver o detalhamento de qual jogador: "))
if jogador_detalhes == 999:
    print("Fim do Programa!")
else:
    #while 0 < jogador_detalhes and jogador_detalhes > (len(jogadores) - 1):
    jogador_detalhes = int(input("Não existe jogador com esse código, tente novamente!"))
    for i in range(len(jogadores)):
        if i == jogador_detalhes:
            print(f'Levantamento do JOGADOR {jogadores[i]["Nome"]}')
            for j in range(len(gols_partida)):
                print(f"No jogo {j} fez {gols_partida[j]} gols")