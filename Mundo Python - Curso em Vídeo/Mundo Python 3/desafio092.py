#Cadastro de Trabalhador em Python
dados = {}
dados["Nome"] = input("Digite o nome: ")
dados["Idade"] = (2024 - int(input("Digite o ano de nascimento: ")))
dados["CPTS"] = int(input("Digite a carteira de trabalho (CPTS): "))
if dados["CPTS"] != 0:
    dados["Ano de Contratação"] = int(input("Digite o ano da primeira contratação: "))
    dados["Salário"] = float(input("Digite o valor do salário atual: R$"))
    dados["Ano para Aposentadoria"] = 35 - (2024 - dados["Ano de Contratação"]) 
    for pos, valor in dados.items():
        print(f"{pos} é {valor}")
else:
    for pos, valor in dados.items():
        print(f"{pos} é {valor}")