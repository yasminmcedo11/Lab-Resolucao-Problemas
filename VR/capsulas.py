#time limit
n, f = map(int, input().split())
ciclos = list(map(int, input().split()))
dinheiro = 0
dias = 0
while dinheiro < f:
    for capsula in ciclos:
        if (dias == capsula or dias % capsula == 0) and dias != 0:
            dinheiro += 1
    dias += 1
print(dias-1)