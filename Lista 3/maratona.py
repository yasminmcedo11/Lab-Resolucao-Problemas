n, m = map(int, input().split())
postos = list(map(int, input().split()))
contador = 0
postos.append(42695)
for i in range(1, n+1):
    if (postos[i] - postos[i-1]) > m:
        contador += 1 
if contador == 0:
    print("S")
else:
    print("N")
#Resposta Errada -> S -- Resposta Certa -> N