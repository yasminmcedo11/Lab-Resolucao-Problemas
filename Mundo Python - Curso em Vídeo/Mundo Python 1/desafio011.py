#Pintando Parede
largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
area = largura*altura
qtd_tinta = area/2
print("A área de parede é {:.2f} m2 e a quantidade de tinta utilizada foi de {:.2f} L".format(area, qtd_tinta))