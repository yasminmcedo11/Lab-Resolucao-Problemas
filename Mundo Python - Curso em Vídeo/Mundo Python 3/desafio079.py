#Valores Únicos em uma Lista
entrada = input("Digite os números que desejar: ").split()
numeros = []
for n in map(int, entrada):
    if n not in entrada:
        numeros.append(n)
print(sorted(numeros))
