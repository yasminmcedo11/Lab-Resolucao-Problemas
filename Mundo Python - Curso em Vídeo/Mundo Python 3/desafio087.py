#Mais sobre Matriz em Python
lista = []
pares = []
soma_pares = 0
soma_colunas = 0
for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite um valor para [{i}, {j}] = "))
        linha.append(numero)
        if numero % 2 == 0:
            pares.append(numero)
    lista.append(linha[:])    
for numero in pares:
    soma_pares += numero
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if j == 2:
            soma_colunas += lista[i][j]
        if i == 1:
            if j == 0:
                maior = lista[i][j]
            else:
                if lista[i][j] > maior:
                    maior = lista[i][j]
print("-"*50)
print(f"""[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]
[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]
[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]""")
print("-"*50)
print(f"""Dados Finais
Soma dos pares digitados -> {soma_pares}
Soma dos valores da 3° coluna -> {soma_colunas}
Maior valor da 2° linha -> {maior}""")
