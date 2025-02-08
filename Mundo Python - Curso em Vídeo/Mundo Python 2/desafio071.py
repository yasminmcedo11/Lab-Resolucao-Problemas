#Simulador de Caixa Eletrônico
n = int(input("Digite o valor que deseja sacar: R$"))
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_1 = 0
while True:
    if n < 50:
        if n < 20:
            if n < 10:
                n = n - 1
                notas_1 += 1
            else:
                n = n - 10  
                notas_10 += 1 
        else:
            n = n - 20
            notas_20 += 1
    else:
        n = n - 50
        notas_50 += 1
    if n == 0:
        break
print(f"Foram necessárias {notas_50} nota(s) de 50, {notas_20} de 20, {notas_10} de 10 e {notas_1} de 1.")
