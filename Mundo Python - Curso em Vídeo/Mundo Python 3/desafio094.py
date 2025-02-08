#Unindo Dicionários e Listas
pessoa = {}
dados = []
acima_media = []
nomes_mulheres = []
soma = 0
while True:
    pessoa["Nome"] = input("Digite o nome: ")
    pessoa["Sexo"] = input("Digite o sexo: [F\M]").lower()[0]
    pessoa["Idade"] = int(input("Digite a idade: "))
    dados.append(pessoa.copy())
    r = input("Deseja continuar? [N\S] ")[0]
    if r not in "Ss":
        break
qtd_cadastros = len(dados)
for i in range(len(dados)):
    soma += dados[i]["Idade"]
media = soma/qtd_cadastros
for i in range(len(dados)):
    if dados[i]["Sexo"] == "f":
        nomes_mulheres.append(dados[i]["Nome"])
    if dados[i]["Idade"] > media:
        acima_media.append(dados[i]["Nome"])
for pessoa in dados:
    for pos, valor in pessoa.items():
        print(f"{pos}: {valor}") 
print(f"Foram {qtd_cadastros} cadastrados, com média de idade {media:.2f}. ")
print(f"As mulheres são {nomes_mulheres}, e os acima da média de idade são {acima_media}")




