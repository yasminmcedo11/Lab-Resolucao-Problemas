#Calculando a média
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1 + n2)/2
if media >= 7:
    print("Sua média foi {:.2f}.".format(media))
    print("Aprovado!")
elif 4.0 <= media <= 6.9: 
    print("Sua média foi {:.2f}.".format(media))  
    print("Em recuperação.")
else:
    print("Sua média foi {:.2f}.".format(media))
    print("Reprovado.")      
