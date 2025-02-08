#Extraindo Dados de uma Lista
numeros = list(map(int, input("Digite os números que desejar: ").split()))
qtd_numeros = len(numeros)
numeros_ordenados = sorted(numeros, reverse = True)
for numero in numeros:
    if numero == 5:
        condicao = 1
        break
    else:
        condicao = 0
print(f"""Dados da Lista:
Quantidade de Números -> {qtd_numeros}
Números Ordenados de Forma Descrente -> {numeros_ordenados}
O número 5 está presente na lista? -> {"Sim" if condicao == 1 else "Não"}""")    