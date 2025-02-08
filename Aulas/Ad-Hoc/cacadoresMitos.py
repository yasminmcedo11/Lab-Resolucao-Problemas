n = int(input())
coordenadas_vistas = []
raio = 0
#coordenadas_vistas = set()
for i in range(n):
    coordenadas = tuple(map(int, input().split()))
    if coordenadas in coordenadas_vistas:
        raio += 1
    coordenadas_vistas.append(coordenadas)    
#for i in range(len(matriz)):
#    for j in range(i + 1, len(matriz)):
#        if (matriz[i] == matriz[j]):
#            raio += 1

print(raio) 
        
