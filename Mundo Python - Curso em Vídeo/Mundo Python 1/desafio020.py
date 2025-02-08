#Sorteando uma ordem na lista
import random

nomes = list(map(str, input("Digite os nomes dos alunos: ").split()))
random.shuffle(nomes)
print("A ordem de apresentação é {}".format(nomes))
