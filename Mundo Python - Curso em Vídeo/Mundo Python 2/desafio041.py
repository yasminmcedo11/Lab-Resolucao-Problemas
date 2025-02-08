#Classificando Atletas
ano = int(input("Digite seu ano de nascimento: "))
if 2024 - ano > 25:
    print("Sua categoria é MASTER.")
elif 19 < (2024 - ano) <= 25:
    print("Sua categoria é SÊNIOR.")
elif 14 < (2024 - ano) <= 19:
    print("Sua categoria é JÚNIOR.")
elif 9 < (2024 - ano) <= 14:
    print("Sua categoria é INFANTIL.")
else: 
    print("Sua categoria é MIRIM.")        