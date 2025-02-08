#Quebrando um número
lista_numero = input("Digite um número: ")
inteiro = []
for i in range(len(lista_numero)):
    inteiro.append(lista_numero[i])
    if lista_numero[i] == ".":
        break
inteiro.remove(".")   
numero_str = " ".join(inteiro)
numero_inteiro = int(numero_str.replace(" ", ""))  #removendo espaços vazios entre os numeros   
print("A porção inteira do número {:.2f} é {}.".format(float(lista_numero), numero_inteiro))
#parte_inteira = math.trunc(n) ou
#numero_inteiro = int(n)