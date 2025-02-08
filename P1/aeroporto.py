#criar uma lista de aeroportos (uma lista de zeros [0,0,0] para os n valores)
# quando um aeroporto for citado, atualizar o valor na lista (associar cada aeroporto ao indice da lista)

while True:
    a, v = map(int, input().split())
    if (a, v) == (0, 0):
        break
    print("Teste")

    contador = [0]*(a+1)
    for i in range(v):
        origem, destino = map(int, input().split())
        contador[origem] += 1
        contador[destino] += 1 
    maior = max(contador)
    elementos = []
    for indice in range(len(contador)):
        if contador[indice] == maior:
            elementos.append(str(indice))
    print(" ".join(elementos) + " ")        

