#10% de erro
posicao_k = int(input())
posicao_l = int(input())
maior_posicao = max(posicao_k, posicao_l)
menor_posicao = min(posicao_k, posicao_l)
if maior_posicao > 8 and menor_posicao < 8:
    print("final")
elif menor_posicao > 8:
    if maior_posicao - menor_posicao == 1:
        if menor_posicao % 2 == 0:
            print("quartas")
        else:
            print("oitavas")
    elif maior_posicao - menor_posicao == 2:
        if maior_posicao < 12:
            print("quartas")
        elif 5 > menor_posicao > 11:
            print("semifinal")
        else:
            print("quartas")
    elif maior_posicao - menor_posicao == 3:
        if menor_posicao % 2 != 0:
            print("quartas")
        else:
            print("semifinal")
    elif maior_posicao - menor_posicao == 4 or maior_posicao - menor_posicao == 5 or maior_posicao - menor_posicao == 6 or maior_posicao - menor_posicao == 7:
        print("semifinal")
else:
    if maior_posicao - menor_posicao == 1:
        if menor_posicao % 2 == 0:
            print("quartas")
        else:
            print("oitavas")
    elif maior_posicao - menor_posicao == 2:
        if maior_posicao < 12:
            print("quartas")
        elif 5 > menor_posicao > 11:
            print("semifinal")
        else:
            print("quartas")
    elif maior_posicao - menor_posicao == 3:
        if menor_posicao % 2 != 0:
            print("quartas")
        else:
            print("semifinal")
    elif maior_posicao - menor_posicao == 4 or maior_posicao - menor_posicao == 5 or maior_posicao - menor_posicao == 6 or maior_posicao - menor_posicao == 7:
        print("semifinal")