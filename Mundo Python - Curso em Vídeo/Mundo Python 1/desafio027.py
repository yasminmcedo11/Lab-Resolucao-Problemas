#Primeiro e último nome
nome = input("Digite o nome completo: ")
nome = nome.split()
print("Primeiro nome: {}. Último nome: {}".format(nome[0], nome[(len(nome)-1)]))