n = int(input())

for i in range(n):
    m = int(input())
    lista_chegada = list(map(int, input().split()))
    lista_ordenada = sorted(lista_chegada, reverse = True)
    contador = 0

    for j in range(len(lista_ordenada)):
        if lista_chegada[j] == lista_ordenada[j]:
            contador += 1
    print(contador)        
