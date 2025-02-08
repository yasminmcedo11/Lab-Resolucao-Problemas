a, g, rendimento_a, rendimento_g = [round(x,2) for x in map(float, input().split())] 

custo_alcool = a * (1/rendimento_a)
custo_gasolina = g * (1/rendimento_g)

if(custo_alcool >= custo_gasolina):
    print("G")
else:
    print("A")    