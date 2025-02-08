#Aumento múltiplos
salario = float(input("Digite o valor do salário: "))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15
print("O seu aumento foi de R${:.2f}, passando a receber R${:.2f}.".format(aumento, salario+aumento))        