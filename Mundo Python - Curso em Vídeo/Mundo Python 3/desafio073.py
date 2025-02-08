#Tuplas com Times de Futebol
classificacao = ("botafogo", "palmeiras", "flamengo", "fortaleza", "internacional", "sao paulo", "corinthians",
"bahia", "cruzeiro", "vasco", "vitoria", "atletico-mg", "fluminense", "gremio", "juventude", "bragantino", 
"athletico-pr", "criciuma", "atletico-go", "cuiaba")
for posicao, time in enumerate(classificacao):
    if posicao == 0 or posicao == 1 or posicao == 2 or posicao == 3 or posicao == 4:
        print(f"{posicao+1}° -> {time}")
    if posicao == 16 or posicao == 17 or posicao == 18 or posicao == 19:
        print(f"{posicao+1}° -> {time}")
print(f"Times ordenados em ordem alfabética: \n{sorted(classificacao)}")    
for i in range(len(classificacao)):
    if classificacao[i] == "vitoria":
        print(f"O Vitória ficou na {i+1}° posição")    
