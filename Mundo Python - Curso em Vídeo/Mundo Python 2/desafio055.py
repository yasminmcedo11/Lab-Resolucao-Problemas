#Maior e Menor da Sequência
pesos = list(map(float, input("Digite o peso de 5 pessoas: ").split()))
maior = max(pesos)  
menor = min(pesos)
print("O maior peso é {:.2f} e menor é {}.".format(maior, menor))