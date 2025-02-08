from itertools import product
p, *livros_portugues = map(int, input().split())
m, *livros_matematica = map(int, input().split())
f, *livros_fisica = map(int, input().split())
q, *livros_quimica = map(int, input().split())
b, *livros_biologia = map(int, input().split())
k = int(input())
conjunto_caro = []
combinacoes = product(livros_portugues, livros_matematica, livros_fisica, livros_quimica, livros_biologia)
for combinacao in combinacoes:
    conjunto_caro.append(sum(combinacao))

conjunto_caro.sort(reverse = True)
soma = sum(conjunto_caro[:k])
print(soma)