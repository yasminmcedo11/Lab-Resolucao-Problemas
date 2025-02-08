#Sorteando um item na lista
import random

nomes = list(map(str, input("Digite os nomes dos alunos: ").split()))
nome_escolhido = random.choice(nomes)
print("O nome escolhido foi {}.".format(nome_escolhido))