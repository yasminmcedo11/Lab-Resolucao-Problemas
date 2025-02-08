#100% de acerto
import math

l, a, p, r = map(int, input().split())
def verificar_caixa(l, a, p, r):
    diag = math.sqrt(l**2 + a**2 + p**2)
    diam = 2 * r
    if diag <= diam:
        print("S")
    else:
        print("N")

verificar_caixa(l,a, p, r)