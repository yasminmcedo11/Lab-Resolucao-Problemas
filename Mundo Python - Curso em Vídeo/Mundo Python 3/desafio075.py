#Análise de Dados em uma Tupla
valores = tuple(map(int, input("Digite 4 números: ").split()))
contador = 0
contador2 = 0
pares = []
for i in range(len(valores)):
    if valores[i] == 9:
        contador += 1
    if contador2 == 0 and valores[i] == 3:
        posicao = i
        contador2 += 1
    if valores[i] % 2 == 0:
        pares.append(valores[i])
print(f"""Dados Finais:
Quantidade de 9 digitados -> {contador}
Posição do 1° valor 3 -> {"Não há valor 3" if contador2 == 0 else posicao}
Números Pares digitados -> {pares}""")
    