#Cadastro de Jogador de Futebol
jogador = {}
gols_total = 0
jogador["Nome"] = input("Digite o nome do jogador: ")
jogador["Partidas Jogadas"] = int(input("Digite a quantidade de partidas jogadas: "))
numero = jogador["Partidas Jogadas"]
for i in range(numero):
    gols_partida = int(input(f"Digite a quantidade de gols feitos na partida {i+1}: "))
    gols_total += gols_partida
jogador["Gols Feitos"] = gols_total
for pos, valor in jogador.items():
    print(f"{pos}: {valor}")