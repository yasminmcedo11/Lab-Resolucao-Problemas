#Analisando Triângulo
a = int(input("Digite a reta A: "))
b = int(input("Digite a reta B: "))
c = int(input("Digite a reta C: "))
if a + b > c and a + c > b and c + b > a:
    print("Formam triângulo :)")
else:
    print("Não formam triângulo :(")    