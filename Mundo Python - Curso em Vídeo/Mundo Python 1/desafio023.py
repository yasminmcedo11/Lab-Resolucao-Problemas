#Separando dígitos de um número
numero = input("Digite um número: ")
if(len(numero) < 2):
    unidade = numero[0]
    dezena = 0
    centena = 0
    milhar = 0
if(2 <= len(numero) < 3):
    unidade = numero[1]
    dezena = numero[0]
    centena = 0
    milhar = 0
if(3 <= len(numero) < 4):
    unidade = numero[2]
    dezena = numero[1]
    centena = numero[0]
    milhar = 0
if(4 <= len(numero) < 5):
    unidade = numero[3]
    dezena = numero[2]
    centena = numero[1]
    milhar = numero[0]      

print("""unidade: {}
dezena: {}
centena: {}
milhar: {}""".format(unidade, dezena, centena, milhar))