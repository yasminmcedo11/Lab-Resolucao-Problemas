#Maior e Menor Valores
continuar = "continuar"
media = 0
contador = 0
soma = 0
lista = []
while continuar == "continuar":
    n = int(input("Digite um número: "))
    soma += n
    contador += 1
    media = soma/contador
    lista.append(n)
    maior = max(lista)
    menor = min(lista)
    continuar = input("Digite continuar para seguir informando números: \n")
print("""Resulato Final
Média -> {:.2f}
Maior Número -> {}
Menor Número -> {}""".format(media, maior, menor))

