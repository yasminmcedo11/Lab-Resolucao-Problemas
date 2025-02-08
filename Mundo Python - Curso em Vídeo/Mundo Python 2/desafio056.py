#Analisador Completo
nome = []
idade = []
sexo = []
media = contador = maior = 0
for i in range(4):
    n = input("Digite o nome: ").strip()
    i = int(input("Digite a idade: "))
    s = input("Digite o sexo: ").lower().strip()
    nome.append(n)
    idade.append(i)
    sexo.append(s)
for i in range(4):
    media += idade[i]       
    if sexo[i] == "mulher" and idade[i] < 20:
        contador += 1
    if idade[i] > maior and sexo[i] == "homem":
        maior = idade[i] 
for i in range(4):
    if maior == idade[i]:
        idade_guardada = i           
media = media/4
print("""A média de idade: {:.2f} 
Nome do homem mais velho: {} 
Mulheres abaixo de 20 anos: {}""".format(media, nome[idade_guardada], contador))        
