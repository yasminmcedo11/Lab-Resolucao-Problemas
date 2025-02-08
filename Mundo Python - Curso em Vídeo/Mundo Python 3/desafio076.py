#Lista de Preços com Tupla
lista = ("Lápis", 1.75, "Borracha", 2.0, "Caderno", 15.90, "Estojo", 25.0, 
"Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
print(f"-"*50)
print("Listagem de Preços")
print(f"-"*50)
for i in range(len(lista)):
    if i % 2 == 0:
        print(f"{lista[i]:.<30} R${(lista[i+1]):.2f}")
print(f"-"*50)