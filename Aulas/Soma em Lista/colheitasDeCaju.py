l, c, m, n = map(int, input().split())
matriz = []
for _ in range(l):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Construção da matriz de soma acumulada (prefix_sum)
max_margaridas = 0
    
    # Percorrer todos os lotes de tamanho MxN
for i in range(l - m + 1):  # Vai de 0 até L - M
    for j in range(c - n + 1):  # Vai de 0 até C - N
        soma = 0
            # Soma as margaridas no lote de 2x1
        for k in range(m):  # Percorre as M linhas do lote
            for l in range(n):  # Percorre as N colunas do lote
                soma += matriz[i + k][j + l]
        max_margaridas = max(max_margaridas, soma)
    
    # Imprime o resultado
print(max_margaridas)