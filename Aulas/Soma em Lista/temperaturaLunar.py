n, m = map(int, input().split())
contador = 1
while n !=0 and m != 0:
    medicoes = []
    soma = []
    for i in range(n):
        medicoes.append(int(input()))
    soma_atual = sum(medicoes[:m])
    soma.append(int(soma_atual/m))
    for i in range(m, n):
        soma_atual += medicoes[i] - medicoes[i - m]
        soma.append((int(soma_atual/m)))
        #soma.append(int((sum(medicoes[i:(i+m)]))/m))
    menor = min(soma)
    maior = max(soma)
    print(f"Teste {contador}")
    print(f"{menor} {maior}")
    contador += 1
    n, m = map(int, input().split())

