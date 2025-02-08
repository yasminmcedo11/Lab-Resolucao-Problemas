#Validando Expressões Matemáticas
expressao = input("Digite a expressão matemática que deseja verificar: ")
parenteses_esquerdo = 0
parenteses_direito = 0
ordem_parenteses = []
for letra in expressao:
    if letra == "(":
        parenteses_direito += 1
        ordem_parenteses.append(letra)
    if letra == ")":
        parenteses_esquerdo += 1 
        ordem_parenteses.append(letra)
condicao = 1
for i in range(len(ordem_parenteses)):
    if (i == 0 and (ordem_parenteses[i] == ")")) or (i == (len(ordem_parenteses)-1) and ordem_parenteses == "("):
        condicao = 0
    
if parenteses_esquerdo == parenteses_direito and condicao == 1:
    print("A expressão está correta")
else:
    print("A expressão está incorreta")       
