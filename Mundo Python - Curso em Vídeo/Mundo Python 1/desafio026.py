#Primeira e última ocorrência de uma string
nome = input("Digite uma frase: ").strip().lower()
qtd_a = nome.count("a")
posicao = []
for i in range(len(nome)):
    if nome[i] == "a":
        posicao.append(i)       
print("""A letra a aparece {} vezes. Aparece a primeira vez na posição {} e a útlima vez na posição {}"""
      .format(qtd_a, min(posicao), max(posicao)))        
#rfind -> procura a primeira ocorrencia partindo do lado direito