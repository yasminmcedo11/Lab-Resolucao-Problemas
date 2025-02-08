n = int(input())
expressao = list(map(str, input().split()))
if expressao[1] == "+":
    valor = int(expressao[0]) + int(expressao[2])
if expressao[1] == "*":
    valor = int(expressao[0]) * int(expressao[2])
if valor > n:
    print("OVERFLOW")
else:
    print("OK")