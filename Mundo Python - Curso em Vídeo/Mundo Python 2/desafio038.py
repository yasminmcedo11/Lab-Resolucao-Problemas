#Comparando números
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
if n1 > n2:
    print("O número {} é maior.".format(n1))
elif n2 > n1:
    print("O número {} é maior.".format(n2))
else:
    print("Os números são iguais, logo não existe valor maior.")        