n, m = map(int, input().split())
matriz = []
matriz_resultados = []
for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)
for i in range(n):
    if n > 1:
        soma_linha = sum(linha[i] for linha in matriz)
        matriz_resultados.append(soma_linha)
        for j in range(m):
            if m > 1:
                soma_coluna = sum(coluna[j] for coluna in matriz)
                matriz_resultados.append(soma_coluna)
            else:
                matriz_resultados.append(matriz[i][j])
    else:
        matriz_resultados.append(matriz[i][0])
        for j in range(m):
            if m > 1:
                soma_coluna = sum(coluna[j] for coluna in matriz)
                matriz_resultados.append(soma_coluna)
            else:
                matriz_resultados.append(matriz[i][j])
maior = max(matriz_resultados)
print(maior)