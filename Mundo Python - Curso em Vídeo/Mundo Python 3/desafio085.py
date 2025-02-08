#Lista com Pares e Ímpares
lista_total = [[], []]
for i in range(7):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        lista_total[0].append(numero)
    else:
        lista_total[1].append(numero)
lista_total[0].sort()
lista_total[1].sort()
print(f"Ordem dos pares: {lista_total[0]}; \nOrdem dos ímpares: {lista_total[1]}")   
