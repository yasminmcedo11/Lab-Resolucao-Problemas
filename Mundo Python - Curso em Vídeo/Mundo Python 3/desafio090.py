#Dicionário em Python
aluno = {}
aluno["Nome"] = input("Digite o nome do aluno: ")
aluno["Media"] = float(input("Digite a média do aluno: "))
if aluno["Media"] > 6:
    aluno["Situação"] = "Aprovado"
if 4 <= aluno["Media"] < 6:
    aluno["Situação"] = "Em recuperação"
if aluno["Media"] < 4:
    aluno["Situação"] = "Reprovado"
for k, v in aluno.items():
    print(f"{k} é {v}")

