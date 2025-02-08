#Conversor de Bases Numéricas
n = int(input("Digite um número: "))
base = input("Digite a base que deseja realizar a conversão: ").lower()
if base == "binario":
    print("O número {} convertido para binário é {}.".format(n, bin(n)[2:]))
elif base == "octal":
    print("O número {} convertido para a base octal é {}.".format(n, oct(n)[2:]))    
elif base == "hexadecimal":
    print("O número {} convertido para base hexadecimal é {}.".format(n, hex(n)[2:]))    
else:
    print("Opção inválida, tente novamente!")    