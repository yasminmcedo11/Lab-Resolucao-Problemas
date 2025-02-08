#Boletim com Listas Compostas
dados_totais = []
r = "s"
while r == "S" or r == "s":
    dados_alunos = []
    dados_alunos.append(input("Digite o nome do aluno: "))
    dados_alunos.append(float(input("Digite a nota da 1° prova: ")))
    dados_alunos.append(float(input("Digite a nota da 2° prova: ")))
    dados_totais.append(dados_alunos[:])
    r = input("Deseja continuar? [N\S]")
boletim = []
for i in range(len(dados_totais)):
    linha = []
    soma = 0
    for j in range(len(dados_totais[i])):
        if j == 0:
            linha.append(dados_totais[i][j])
        if j == 1 or j == 2:
            soma += dados_totais[i][j]
    linha.append(soma/2)
    boletim.append(linha[:])
print("-"*60)
print("""Dados Boletim""")
print("-"*60)
for i in range(len(boletim)):
    print(f"Nome: {boletim[i][0]} -----> Média: {boletim[i][1]:.2f}")
nome = input("Deseja mostrar as notas de qual aluno em específico? ").strip().lower()
for i in range(len(dados_totais)):
    for j in range(len(dados_totais)):
        if dados_totais[i][j] == nome:
            print(f"Notas de {dados_totais[i][j]}: {dados_totais[i][1:3]}")




