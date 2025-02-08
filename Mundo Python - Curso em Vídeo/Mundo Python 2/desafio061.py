#Progressão Aritmética v2.0
termo_1 = float(input("Digite o primeiro termo da PA: "))
razao = float(input("Digite a razão da PA: "))
print("1° termo = {}".format(termo_1))
n = 1
termo_i = termo_1
while n != 10:
    termo_i += razao
    print("{}° termo = {}".format(n+1, termo_i))
    n += 1
