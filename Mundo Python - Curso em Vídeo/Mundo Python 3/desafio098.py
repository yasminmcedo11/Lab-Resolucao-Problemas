#Função de Contador
def contador(inicio, fim, passo):
    print("-"*60)
    print(f"Contando de {inicio} até {fim}, de {passo} em {passo}.")
    if inicio > fim:
        for i in range(inicio, fim-1, -passo):
            print(i, end =" ")
    else:
        for i in range(inicio, fim+1, passo):
            print(i, end =" ")
    print()

contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é a sua vez de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
contador(i, f, p)
