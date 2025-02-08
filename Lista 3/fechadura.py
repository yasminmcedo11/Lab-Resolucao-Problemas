n, m = map(int, input().split())
altura_pinos = list(map(int, input().split()))
movimentos = 0
while True:
    #if altura_pinos[len(altura_pinos)-1] > m and 
    if altura_pinos[0] > m:
        movimentos = altura_pinos[0] - m
        altura_pinos[0] = m
        altura_pinos[1] += movimentos
    if altura_pinos[0] < m:
        movimentos = m - altura_pinos[0]
        altura_pinos[0] = m
        altura_pinos[1] += movimentos
    if altura_pinos[n-1] > m and altura_pinos[n-2] < m:
        movimentos = altura_pinos[n-1] - m
        altura_pinos[n-1] = m
    if altura_pinos[n-1] < m and altura_pinos[n-2] > m:
        movimentos = m - altura_pinos[n-1]
        altura_pinos[n-1] = m
    for i in range(1,len(altura_pinos)-1):
        if (altura_pinos[i] > m and altura_pinos[i+1] > m) or (altura_pinos[i] > m and altura_pinos[i-1] < m):
            altura_pinos[i] -= 1
            altura_pinos[i+1] -= 1
            movimentos += 1
        if (altura_pinos[i] < m and altura_pinos[i+1] < m) or (altura_pinos[i] < m and altura_pinos[i-1] > m):
            altura_pinos[i] += 1
            altura_pinos[i+1] += 1
            movimentos += 1
    soma = (sum(altura_pinos))/len(altura_pinos)
    #soma = soma/len(altura_pinos)
    print(soma)
    if (soma == m): #and len(set(altura_pinos)) == 1:
        break
print(altura_pinos)
print(movimentos)
