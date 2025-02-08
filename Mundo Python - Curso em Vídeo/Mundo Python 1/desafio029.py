#Radar Eletrônico
velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print("Você foi multado em R${:.2f}.".format(multa))
else:
    print("Você não foi multado. :)")    