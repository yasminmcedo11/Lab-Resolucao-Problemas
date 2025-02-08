#Detector de Palíndromo
frase = input("Digite uma frase: ").strip().lower()
frase = frase.replace(" ", "")
contador = 0
for i in range(int(len(frase)/2)):
    if frase[i] == frase[len(frase)-i-1]:
        contador += 1
if contador == int((len(frase))/2):
    print("É palíndromo!")
else:
    print("Não é palíndromo!")            

