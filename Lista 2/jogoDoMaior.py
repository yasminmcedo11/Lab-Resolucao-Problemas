n = int(input())
while n != 0:
    vencedores = []
    vitorias_a = 0
    vitorias_b = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a > b:
            vencedores.append("a")
        if b > a:
            vencedores.append("b")
    for vencedor in vencedores:
        if vencedor == "a":
            vitorias_a += 1
        if vencedor == "b":
            vitorias_b += 1
    print(f"{vitorias_a} {vitorias_b}") 
    n = int(input())   


