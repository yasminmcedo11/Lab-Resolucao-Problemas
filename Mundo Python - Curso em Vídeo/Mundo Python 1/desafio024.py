#Verificando as primeiras letras de um texto
cidade = input("Digite o nome da cidade: ")
cidade = cidade.lower().lstrip()
if "santo" in cidade[:5]:
    print("Está")
else:
    print("Não está")    