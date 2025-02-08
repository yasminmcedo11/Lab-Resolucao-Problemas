#Gerenciador de Pagamentos
preco = float(input("Digite o preço do produto: R$"))
print("""Para as condições de pagamento:
      Digite 1: Pagamento à vista dinheiro/cheque
      Digite 2: Pagaemtno à vista no cartão
      Digite 3: Pagamento em até 2x no cartão
      Digite 4: Pagamento em 3x ou mais vezes no cartão""")
condicao = int(input("Digite a opção desejada: "))
if condicao == 1:
    preco = preco - (preco*0.10)
    print("O preço a ser pago é R${:.2f}.".format(preco))
if condicao == 2:
    preco = preco - (preco*0.05)
    print("O preço a ser pago é R${:.2f}.".format(preco))
if condicao == 3:
    print("O preço a ser pago é R${:.2f}.".format(preco))
if condicao == 4:   
    preco = preco + (preco*0.20)
    print("O preço a ser pago é R${:.2f}.".format(preco))         