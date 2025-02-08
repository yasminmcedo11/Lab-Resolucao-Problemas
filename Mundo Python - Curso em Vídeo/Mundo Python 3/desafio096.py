#Função que Calcula Área
def calcular_area(a, b):
    area = a * b
    print(f"A área do terreno é {area:.2f} m2")

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
calcular_area(largura, comprimento)