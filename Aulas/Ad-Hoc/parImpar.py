n = int(input()) #numero de partidas
numero_teste = 1
while (n != 0):
    jogador1 = input()  #nome do jogador 1
    jogador2 = input()  #nome do jogador 2
    print("Teste {}".format(numero_teste))
    for i in range(n):
        escolha1, escolha2 = map(int, input().split())
        resultado_final = escolha1 + escolha2
        if (resultado_final%2 == 0):
            print(jogador1)
        else:
            print(jogador2)
    print()        
    numero_teste += 1
    n = int(input())