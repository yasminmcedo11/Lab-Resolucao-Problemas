#Tabuada v3.0
n = int(input("Digite um número: "))
while True:
    if n < 0:
        break
    lista_numeros = []
    for i in range(1, 11):
        lista_numeros.append(n*i)
    print("-"*30)    
    for i in range(len(lista_numeros)):
        print("{} x {} = {}".format(n, i+1, lista_numeros[i]))
    n = int(input("Digite um número: ")) 
print("FIM!")   