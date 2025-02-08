i, n = map(int, input().split())
dinheiro_D = i
dinheiro_E = i
dinheiro_F = i
for i in range(n):
    operacao = list(map(str, input().split()))
    if len(operacao) == 3:
        if operacao[0] == "C":
            if operacao[1] == "D":
                dinheiro_D -= int(operacao[2]) 
            if operacao[1] == "E":
                dinheiro_E -= int(operacao[2])
            if operacao[1] == "F":
                dinheiro_F -= int(operacao[2])
        if operacao[0] == "V":
            if operacao[1] == "D":
                dinheiro_D += int(operacao[2]) 
            if operacao[1] == "E":
                dinheiro_E += int(operacao[2])
            if operacao[1] == "F":
                dinheiro_F += int(operacao[2])
    
    if len(operacao) == 4:
        if operacao[1] == "D":
            if operacao[2] == "E":
                dinheiro_D += int(operacao[3])
                dinheiro_E -= int(operacao[3])
            if operacao[2] == "F":
                dinheiro_D += int(operacao[3])
                dinheiro_F -= int(operacao[3])
        if operacao[1] == "E": 
            if operacao[2] == "D":
                dinheiro_E += int(operacao[3])
                dinheiro_D -= int(operacao[3])
            if operacao[2] == "F": 
                dinheiro_E += int(operacao[3])
                dinheiro_F -= int(operacao[3])
        if operacao[1] == "F":
            if operacao[2] == "D":
                dinheiro_F += int(operacao[3])
                dinheiro_D -= int(operacao[3])
            if operacao[2] == "E": 
                dinheiro_F += int(operacao[3])
                dinheiro_E -= int(operacao[3])
print(f"{dinheiro_D} {dinheiro_E} {dinheiro_F}")


