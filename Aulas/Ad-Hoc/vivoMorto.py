p, r = map(int, input().split())
numero_teste = 1
while (p != 0) and (r != 0):
    ordem_fila = list(map(int, input().split()))

    for i in range(r):
        n, j, *escolhas = [int(x) for x in input().split()]
        itens_removidos = []
        for i in range(n):
            if escolhas[i] != j:
                itens_removidos.append(ordem_fila[i])
        for i in range(len(itens_removidos)):
            ordem_fila.remove(itens_removidos[i])        
        if len(ordem_fila) == 1:
            vencedor = ordem_fila[0]
    print("Teste {}".format(numero_teste)) 
    numero_teste += 1
    print(vencedor)
    print()
    p, r = map(int, input().split())


            
    
