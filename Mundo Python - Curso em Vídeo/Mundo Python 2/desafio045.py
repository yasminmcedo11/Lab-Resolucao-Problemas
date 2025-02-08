#GAME: Pedra, Papel e Tesoura
import random

print("""Suas opçoes:
      [0] -> Pedra
      [1] -> Papel
      [2] -> Tesoura""")
opcao_usuario = int(input("Digite a opção desejada: "))
opcao_computador = random.randint(0,2)
if opcao_usuario == opcao_computador:
    print("Empate! Ambos escolheram a mesma opção.")
if opcao_usuario == 0 and opcao_computador == 1:
    print("O computador venceu.")
if opcao_usuario == 0 and opcao_computador == 2:
    print("O usuário venceu.")   
if opcao_usuario == 1 and opcao_computador == 2:
    print("O computador venceu.")
if opcao_usuario == 1 and opcao_computador == 0:
    print("O usuário venceu.")
if opcao_usuario == 2 and opcao_computador == 0:
    print("O computador venceu.")
if opcao_usuario == 2 and opcao_computador == 1:
    print("O usuário venceu.")                
