#Função que Descobre o Maior
def maior (*numeros):
    maior = max(*numeros)
    qtd_numeros = len(*numeros)
    print(f"A quantidade de números digitados foi de {qtd_numeros}")
    print(f"O maior valor é {maior}")

n = tuple(map(int, input("Digite os números que deseja analisar: ").split()))
maior(n)    