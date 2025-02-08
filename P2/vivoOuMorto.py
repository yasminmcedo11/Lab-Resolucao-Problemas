#100% de acerto
p, r = map(int, input().split())
contador = 1
while p != 0 and r != 0:
    fila = list(map(int, input().split()))
    for i in range(r):
        excluidos = []
        matriz_nova = []
        n, j, *acao = map(int, input().split())
        for z in range(len(acao)):
            if acao[z] != j:
                excluidos.append(z)
            else:
                excluidos.append(-1)
        contagem = 0
        for x in range(len(acao)):
            if excluidos[x] != x and contagem == 0:
                matriz_nova.append(fila[x])
        fila = matriz_nova[:]
    print(f"Teste {contador}")
    print(fila[0])
    print()
    contador += 1
    p, r = map(int, input().split())