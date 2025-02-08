#Grupo da Maioridade
pessoas = list(map(int, input("Digite a data de nascimento de 6 pessoas: ").split()))
menor = 0
maior = 0
for i in range(len(pessoas)):
    if (2024 - pessoas[i]) < 18:
        menor += 1
    else:
        maior += 1
print("Existem {} pessoas maiores de idade e {} menores de idade.".format(maior, menor))            
