#Criando um Menu de Opções
print("""Menu de Opções: 
[1] -> Somar
[2] -> Multiplicar
[3] -> Maior
[4] -> Novos Números
[5] -> Sair do Programa     """)
opcao = int(input("Digite a opção desejada: "))
n1, n2 = map(int, input("Digite 2 números: ").split())
while opcao != 5:
    if opcao == 1:
        resultado = n1 + n2
        print("O resultado obtido foi {}".format(resultado))
    if opcao == 2:
        resultado = n1 * n2
        print("O resultado obtido foi {}".format(resultado))
    if opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print("O maior número é {}".format(maior))    
    if opcao == 4:
        n1, n2 = map(int, input("Digite 2 números: ").split()) 
    opcao = int(input("Digite a opção desejada: "))   
print("Fim do Programa!")                  
