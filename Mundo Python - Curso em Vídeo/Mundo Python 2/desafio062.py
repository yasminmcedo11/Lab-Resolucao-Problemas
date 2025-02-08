#Super Progressão Aritmética v3.0
termo_1 = float(input("Digite o primeiro termo da PA: "))
razao = float(input("Digite a razão da PA: "))
n_termos = int(input("Digite o números de termos da PA que deseja saber: "))
print("1° termo = {}".format(termo_1))
n = 1
termo_i = termo_1
while n_termos != 0:
    while n != n_termos:
        termo_i += razao
        print("{}° termo = {}".format(n+1, termo_i))
        n += 1
    n_termos = int(input("Digite quantos números de termos da PA que deseja saber a mais: "))
    n = 0
