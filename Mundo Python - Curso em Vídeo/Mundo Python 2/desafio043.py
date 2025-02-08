#Índice de Massa Corporal 
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em m): "))
imc = peso/(altura**2)
print("Seu IMC é {:.1f}.".format(imc))
if imc < 18.5:
    print("Você está abaixo do Peso Ideal.")
elif 18.5 <= imc < 25:
    print("Você está dentro do Peso Ideal.")
elif 25 <= imc < 30:
    print("Você está com Sobrepeso.")
elif 30 <= imc < 40:
    print("Você está com Obesidade.")    
else:
    print("Você está com Obesidade Mórbida.")

