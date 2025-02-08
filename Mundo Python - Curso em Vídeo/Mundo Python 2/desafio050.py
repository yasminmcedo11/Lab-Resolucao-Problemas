#Soma dos pares
numeros = list(map(int, input("Digite 6 números: ").split()))
soma = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        soma += numeros[i]
if soma == 0:
    print("Valor Desconsiderado.")
else:
    print("A Soma dos números pares é {}.".format(soma))    
