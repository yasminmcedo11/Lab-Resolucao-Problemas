n, m = map(int, input().split())  
altura_pinos = list(map(int, input().split()))  
movimentos = 0
for i in range(n - 1):
    diferenca = m - altura_pinos[i]
    altura_pinos[i] += diferenca
    altura_pinos[i + 1] += diferenca
    movimentos += abs(diferenca)
print(movimentos)