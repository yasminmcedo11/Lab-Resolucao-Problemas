n = int(input())
numero_teste = 1

def descobrir_senha(senha, numeros_associados):
    letra_A = []
    letra_B = []
    letra_C = []
    letra_D = []
    letra_E = []
    senha_real = []
    letra_A.append(numeros_associados[0])
    letra_A.append(numeros_associados[1])
    letra_B.append(numeros_associados[2])
    letra_B.append(numeros_associados[3])
    letra_C.append(numeros_associados[4])
    letra_C.append(numeros_associados[5])
    letra_D.append(numeros_associados[6])
    letra_D.append(numeros_associados[7])
    letra_E.append(numeros_associados[8])
    for i in range(len(senha)):
        if(senha[i] == 'A'):
            senha_real.append(letra_A[0])
        if(senha[i] == 'B'):
            senha_real.append(letra_B[0])
        if(senha[i] == 'C'):
            senha_real.append(letra_C[0])
        if(senha[i] == 'D'):
            senha_real.append(letra_D[0])
        if(senha[i] == 'E'):
            senha_real.append(letra_E[0])

    return senha_real

while (n != 0):
    valores = list(map(str, input().split()))
    #valores2 = list(map(str, input().split()))
    numeros_associados = []
    senha = []
    senha_real = []
    print("Teste {}".format(numero_teste))
    for i in range(16):
        if (i < 11):
            numeros_associados.append(valores[i])
        else:
            senha.append(valores[i])
    
    senha_real = descobrir_senha(senha, numeros_associados)
    print(senha_real)
    print()
    numero_teste += 1
    n = int(input())  