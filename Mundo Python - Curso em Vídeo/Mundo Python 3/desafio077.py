#Contando Vogais em Tuplas
palavras = ("aprender", "programar", "linguagem", "python", "curso", "gratis", "estudar",
"praticar", "trabalhar", "mercado", "programador", "futuro")
for palavra in palavras:
    vogais = []
    for letra in palavra:
        if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
            vogais.append(letra)
    vogais_texto = " ".join(vogais)
    print(f"Na palavra {palavra.upper()} temos as vogais {vogais_texto}")

