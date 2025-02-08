#Lista Completa e Análise de Dados
lista_total = []
while True:
    dados = []
    dados.append(input("Digite o nome: "))
    dados.append(float(input("Digite ao peso: ")))
    lista_total.append(dados[:])
    dados.clear()
    r = input("Deseja continuar? [N\S]")
    if r not in "sS":
        break
qtd_cadastros = len(lista_total)
mais_pesado = max(sublista[1] for sublista in lista_total)
mais_leve = min(sublista[1] for sublista in lista_total)
nomes_pesados = []
nomes_leves = []
for i in range(len(lista_total)):
    for j in range(len(lista_total[i])):
        if lista_total[i][j] == mais_pesado:
            nomes_pesados.append(lista_total[i][0])
        if lista_total[i][j] == mais_leve:
            nomes_leves.append(lista_total[i][0])  
print(f"""Dados Finais:
Quantidade de pessoas cadastradas -> {qtd_cadastros}
Nome dos mais pesados -> {nomes_pesados}
Nome dos mais leves -> {nomes_leves}""") 

