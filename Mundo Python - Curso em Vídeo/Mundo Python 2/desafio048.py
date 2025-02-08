#Soma de Ímpares múltiplos de 3
contador = 0
for i in range(1, 501):
    if (i % 2 != 0) and (i % 3 == 0):
        contador += i
print("A soma de todos os números ímpares entre 1 e 500 é {}.".format(contador))