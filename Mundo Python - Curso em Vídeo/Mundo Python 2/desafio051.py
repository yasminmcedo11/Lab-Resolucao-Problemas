#Progressão Aritmética
termo_1 = float(input("Digite o primeiro termo da PA: "))
razao = float(input("Digite a razão da PA: "))
print("1° termo = {}".format(termo_1))
for i in range(2, 11):
    termo_i = termo_1 + (i - 1) * razao
    print("{}° termo = {}".format(i, termo_i))