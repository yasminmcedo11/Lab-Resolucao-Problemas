n = int(input()) #numero de participantes
numero_teste = 1
while n != 0:
    ordem_entrada = list(map(int, input().split()))
    lista_comparacao = []
    vencedor = 0
    for i in range(1,n+1):
        lista_comparacao.append(i)
    for i in range(len(ordem_entrada)):
        if(ordem_entrada[i] == lista_comparacao[i]):
            vencedor = i+1

    print("Teste {}".format(numero_teste))
    print(vencedor)
    print()

    numero_teste += 1
    n = int(input())




#y = []
#lista_teste = []
#for i in range(1, x+1):
#    z = input(int())
#    y.append(z)

#for i in range(1, x+1):
    #criando lista ordenada para comparaçao
#    lista_teste.append(i)
    
#for i in range(0, x):
    #comparando valores dentro da lista
#    if (lista_teste[i] == y[i]):
#        ganhador = i+1

#print(ganhador)    