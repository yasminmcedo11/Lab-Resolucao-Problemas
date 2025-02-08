x1, y1, x2, y2 = map(int, input().split())

cruzamentos_x = abs(x2 - x1)
cruzamentos_y = abs(y2 - y1)

numero_cruzamentos = cruzamentos_x + cruzamentos_y

print(numero_cruzamentos)