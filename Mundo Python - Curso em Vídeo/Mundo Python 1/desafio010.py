#Conversor de Moedas
#Cotação de dólar atual: 6,17
n = float(input("Digite o valor em reais: R$"))
valor_dolar = n/6.17
print("Com R${:.2f} você consegue comprar ${:.2f} doláres.".format(n, valor_dolar))