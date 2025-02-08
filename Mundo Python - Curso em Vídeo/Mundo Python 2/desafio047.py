#Contagem de Pares
contador = 0
for i in range(1, 51):
    if i % 2 == 0:
        contador += 1
print("Existem {} números pares no intervalo de 1 a 50.".format(contador))        