#Calculando Descontos
preco = float(input("Digite o preço: R$"))
desconto = preco*0.05
preco_final = preco - desconto
print("O preço com desconto é R${:.2f}".format(preco_final))