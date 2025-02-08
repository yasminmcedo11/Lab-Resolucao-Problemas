#Validação de Dados
sexo = input("Digite o sexo: [M/F]  ").strip().upper()[0]
while sexo not in "MF":
    sexo = input("Dados Inválidos, digite novamento seu sexo: ").strip().upper()[0]
print("Sexo {} registrado com sucesso!".format(sexo))



