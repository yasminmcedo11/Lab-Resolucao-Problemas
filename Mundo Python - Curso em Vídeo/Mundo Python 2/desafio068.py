#Jogo do Par ou Ímpar
import random

escolha = int(input("Escolha 1 para Par e 2 para Ímpar: "))
n1_usuario = int(input("Digite um número de 0 a 6: "))
n2_computador = random.randint(0, 6)
vitorias = 0
while True:
    numero = n1_usuario + n2_computador
    if escolha == 1:
        if numero % 2 == 0:
            vitorias += 1
        else:
            break
    if escolha == 2:
        if numero % 2 != 0:
            vitorias += 1
        else:
            break
    escolha = int(input("Escolha 1 para Par e 2 para Ímpar: "))
    n1_usuario = int(input("Digite um número de 0 a 6: "))
    n2_computador = random.randint(0, 6)        
print(f"Você obteve {vitorias} vitória(s) consecutiva(s).")



        