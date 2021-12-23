#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.

times = ('America-MG', 'Athletico-PR', 'Atletico-GO', 'Atletico-MG', 'Bahia', 'Ceará-SC', 'Chapecoense', 'Corinhians', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Grêmio', 'Internacional', 'Juventus', 'Palmeiras', 'Bragantino', 'Santos', 'Sport recife', 'São Paulo')
localização= len(times[0:7])
print(f"Os últimos quatro colocados foram: {times[16:21]}")
print(f"Os cinco primeiros times são: {times[0:5]}")
print(f"Os times em ordem alfabética fica: {sorted(times)}")
print(f"O time da Chapecoense está na posição {localização}")