#Alistamento Militar
ano_nascimento = int(input("Digite seu ano de nascimento: "))
if (2024 - ano_nascimento) < 18:
    print("Faltam {} anos para você se alistar.".format(18-(2024-ano_nascimento)))
elif (2024 - ano_nascimento) == 18:
    print("Você deve se alistar esse ano!")
else: 
    print("Você já ultrapassou o tempo de se alistar há {} anos.".format((2024-ano_nascimento)-18))        