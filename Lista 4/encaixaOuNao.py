n = int(input())
for i in range(n):
    lista = []
    numero, numero_comparado = map(str, input().split())
    lista_digitos = [int(digito) for digito in numero]
    lista_comparado = [int(digito) for digito in numero_comparado]
    x = len(lista_comparado)
    z = len(lista_digitos)
    y = lista_digitos[(z-x):]
    numero_modificado = "".join(map(str, y))
    numero_modificado = int(numero_modificado)
    if int(numero_comparado) == numero_modificado:
        print("encaixa")
    else:
        print("nao encaixa")    

