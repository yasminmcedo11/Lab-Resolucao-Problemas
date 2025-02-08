#Tabuada 
n = int(input("Digite um número: "))
lista_numeros = []
for i in range(1, 11):
    lista_numeros.append(n*i)
print("-"*30)    
for i in range(len(lista_numeros)):
    print("{} x {} = {}".format(n, i+1, lista_numeros[i]))
print("-"*30)   