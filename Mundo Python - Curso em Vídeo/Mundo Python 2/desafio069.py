#Análise de Dados do Grupo
maiores = 0
homens = 0
mulheres_idade = 0
while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo: ").strip().upper()[0]
    if idade > 18:
        maiores += 1
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20:
        mulheres_idade += 1   
    continuar = int(input("Digite 1 para continuar e 2 para encerrar o programa: "))         
    if continuar == 2:
        break
print(f"""Dados do Grupo:
Maiores de Idade -> {maiores}
Homens -> {homens} 
Mulheres abaixo de 20 anos -> {mulheres_idade}""")