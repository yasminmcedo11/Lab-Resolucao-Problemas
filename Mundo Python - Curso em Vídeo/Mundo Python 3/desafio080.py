#Lista Ordenada sem Repetições
lista = []
for i in range(5):
    if i == 0:
        numero = int(input(f"Digite o número {i+1}: "))
        lista.append(numero)
    else:
        numero = int(input(f"Digite o número {i+1}: "))       
        contador = 0
        for i in range(len(lista)):
            if numero < lista[i] and contador == 0:
                if numero not in lista:
                    lista.insert(i, numero)
                    contador += 1
            if i == (len(lista)-1) and numero > lista[len(lista)-1] and contador == 0:
                if numero not in lista:
                    lista.append(numero)   
print(lista)