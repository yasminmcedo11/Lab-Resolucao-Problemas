#Tratando vários valores v1.0
n = int(input("Digite um número: "))
soma = 0
contador = 0
while n != 999:
    soma += n
    contador += 1
    n = int(input("Digite um número: "))
print("A soma dos {} números digitados foi de {}".format(contador, soma))