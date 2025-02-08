#Analisador de Textos
nome = input("Digite o nome completo: ")
nome_minusculo = nome.lower()
nome_maiscula = nome.upper()
contador = 0
for i in range(len(nome)):
    if nome[i] == " ":
        contador += 1
numero_letras = len(nome) - contador  
verificador = 0 
for i in range(len(nome)):
    if nome[i] == " ":
        verificador = i
        break
print("""O nome todo maisculo é {}. Todo minusculo é {}. Quatidade de letras que o nome possui é {}.
O primeiro nome é {}""".format(nome_maiscula, nome_minusculo, numero_letras, nome[:verificador+1]))    
