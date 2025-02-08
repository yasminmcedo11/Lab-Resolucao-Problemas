#Vários Números com Flag
soma = 0
contador = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    soma += n
    contador += 1
print(f"A soma dos {contador} números digitados foi de {soma}.")    