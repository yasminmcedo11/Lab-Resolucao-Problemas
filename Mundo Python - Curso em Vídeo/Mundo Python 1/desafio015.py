#Aluguel de Carros
qtd_dias = int(input("Digite a quantidade de dias alugados: "))
km_rodados = float(input("Digite a quantidade de km rodados: "))
preco = (60*qtd_dias) + (0.15*km_rodados)
print("O preço total é de R${:.2f}.".format(preco))