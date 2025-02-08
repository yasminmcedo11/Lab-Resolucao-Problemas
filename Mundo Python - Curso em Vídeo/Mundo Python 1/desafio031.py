#Custo da Viagem 
distancia = float(input("Digite o valor da dsitância da viagem: "))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print("O preço final da viagem foi de R${:.2f}".format(preco))        
