r_hexadecimal = input() #vermelho
g_hexadecimal = input() #verde
b_hexadecimal = input() #azul
r = int(r_hexadecimal, 16)
g = int(g_hexadecimal, 16)
b = int(b_hexadecimal, 16)
etiquetas_vermelhas = 1
etiquetas_verdes = int(r/g)**2
etiquetas_azuis = int(g/b)**2
etiquetas_totais = int(etiquetas_vermelhas + etiquetas_verdes + (etiquetas_azuis*etiquetas_verdes))
print(hex(etiquetas_totais)[2:])


