#Matriz em Python
lista = []
for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite um valor para [{i}, {j}] = "))
        linha.append(numero)
    lista.append(linha[:])    
print(f"""[ {lista[0][0]} ] [ {lista[0][1]} ] [ {lista[0][2]} ]
[ {lista[1][0]} ] [ {lista[1][1]} ] [ {lista[1][2]} ]
[ {lista[2][0]} ] [ {lista[2][1]} ] [ {lista[2][2]} ]""")