#Estatística em Produtos
total_gasto = 0
produtos_caros = 0
precos = []
nomes = []
while True:
    p = float(input("Digite o preço do produto: R$"))
    n = input("Digite o nome do produto: ")
    precos.append(p)
    nomes.append(n)
    total_gasto += p
    if p > 1000:
        produtos_caros += 1
    barato = min(precos)
    for i in range(len(precos)):
        if barato == precos[i]:
            nome_guardado = i
    continuar = int(input("Digite 1 para continuar e 2 para encerrar o programa: "))
    if continuar == 2:
        break
print(f"""Dados dos Produtos
Total Gasto -> R${total_gasto:.2f}
Produtos com Custo maior que R$1000,00 -> {produtos_caros}
Produto mais Barato -> {nomes[nome_guardado]}""")        
