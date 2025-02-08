t = int(input())
for i in range(t):
    n_instrucoes = int(input())
    instrucoes = []
    p = 0
    for i in range(n_instrucoes):
        instrucao = input()
        instrucoes.append(instrucao[:])
        if instrucoes[i] == "LEFT":
            p -= 1
        if instrucoes[i] == "RIGHT":
            p += 1
        if len(instrucao.split()) > 1:
            numero = instrucao.split()[2:3]
            instrucao_real = instrucoes[(int(numero[0]))-1]
            if instrucao_real == "LEFT":
                instrucoes[i] = "LEFT"
                p -= 1
            if instrucao_real == "RIGHT":
                instrucoes[i] = "RIGHT"
                p += 1
    print(p)