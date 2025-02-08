mensagem = input()
crib = input()
matriz = []
contador = 0
x= len(mensagem) - (len(crib)-1)
for i in range(x):
    linha = []
    contador = i
    invertido = 0
    for j in range(x):
        if contador > 0 or invertido == -1:
            linha.append("0")
        if contador == 0 and invertido == 0:
            linha.extend(crib)
            invertido = -1  
        contador -= 1
    matriz.append(linha)  
crib_ = 0
for i in range(len(matriz)):
    repetido = 0
    for j in range(len(matriz[i])):
        if matriz[i][j] == mensagem[j]:
            repetido += 1
    if repetido > 0:
        crib_ += 1
crib_ = (len(matriz) - crib_) 
print(crib_)


