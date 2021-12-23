palavras = ('America-MG', 'Athletico-PR', 'Atletico-GO', 'Atletico-MG', 'Bahia', 'Ceará-SC', 'Chapecoense', 'Corinhians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventus', 'Palmeiras', 'Bragantino', 'Santos', 'Sport recife', 'São Paulo')
for p in palavras:
    print(f"\n Na palavra {p.upper()} temos ", end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end = '')