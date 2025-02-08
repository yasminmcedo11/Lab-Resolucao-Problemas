#Número por Extenso
numeros_extensos = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze",
"doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
n = int(input("Digite um número entre 0 e 20: "))
while n not in range(0, 21):
    n = int(input("Entrada enválida. Digite um número entre 0 e 20: "))
for posicao, numero in enumerate(numeros_extensos):
    if n == posicao:
        print(f"Você digitou o número {numero}.")
