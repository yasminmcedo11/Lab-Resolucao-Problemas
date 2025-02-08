#Sequência de Fibonacci v1.0
n = int(input("Digite a quantidade de números da Sequência de Fibonacci que deseja saber: "))
contador = 0
s = []
while n != contador:
    if contador == 0:
        s.append(0)
    elif contador == 1:
        s.append(1)
    else:
        numero = s[contador - 2] + s[contador - 1]
        s.append(numero)
    contador += 1    
print("A sequência de Fibonacci é {}".format(s))
