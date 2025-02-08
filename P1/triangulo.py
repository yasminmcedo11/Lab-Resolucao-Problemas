a, b, c, d = map(int, input.split())

def triangulo_possivel(a1, a2, a3):
    return a1 + a2 > a3 and a1 + a3 > a2 and a2 + a3 > a1
