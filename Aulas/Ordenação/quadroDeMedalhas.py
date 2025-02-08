n = int(input())
lista_paises = []
def ordenar_itens(n):
    return (-n[1], -n[2], -n[3], n[0])

for i in range(n):
    paises = list(map(str, input().split()))
    paises = [paises[0]] + list(map(int, paises[1:]))
    lista_paises.append(paises)

lista_ordenada = sorted(lista_paises, key = ordenar_itens)
for pais in lista_ordenada:
    print(" ".join(map(str, pais)))

