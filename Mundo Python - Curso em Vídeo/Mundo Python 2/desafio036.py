#Aprovando Empréstimo
valor_casa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite o salário do comprador: R$"))
anos_pagamento = int(input("Digite a quantidade de anos de financiamento: "))

prestacao_mensal = valor_casa/(anos_pagamento*12)
if prestacao_mensal > 0.30*salario:
    print("Empréstimo negado!")
    print("A prestação mensal será de R${:.2f}, ultrapassando os 30% do salário mensal.".format(prestacao_mensal))
else:
    print("Empréstimo concedido")    
    print("A prestação mensal será de R${:.2f}.".format(prestacao_mensal))