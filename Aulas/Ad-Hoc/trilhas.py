def calcula_esforco(trilha):
    esforco = 0
    anterior = trilha[0]
    for elemento in trilha[1:]:
        if elemento > anterior:
            esforco += (elemento - anterior)
        anterior = elemento
    return esforco

melhor_trilha = 0
melhor_esforco = float('inf')

nt = int(input())
for i in range(nt):
    #trilha = list(map(int, input().split()[1:]))
    #trilha = [int(x) for x in input().split()[1:]]
    qtd, *trilha = [int(x) for x in input().split()]
    
    esforco_ida = calcula_esforco(trilha)
    esforco_volta = calcula_esforco(trilha[::-1])
    if esforco_ida < melhor_esforco:
        melhor_esforco = esforco_ida
        melhor_trilha = i + 1
    if esforco_volta < melhor_esforco:
        melhor_esforco = esforco_volta
        melhor_trilha = i + 1
    
print(melhor_trilha)