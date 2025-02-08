#Analisando Triângulos
a = int(input("Digite a reta A: "))
b = int(input("Digite a reta B: "))
c = int(input("Digite a reta C: "))
if a + b > c and a + c > b and c + b > a:
    if a == b == c:
        print("Formam triângulo equilátero.")
    elif (a == b) or (b == c):
        print("Formam triângulo isósceles.")    
    elif a != b != c:
        print("Formam triângulo escaleno")     
else:
    print("Não formam triângulo :(")    