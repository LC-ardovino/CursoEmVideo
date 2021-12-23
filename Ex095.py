jogador = dict()
partidas = list()
times = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas o jogador {jogador['nome']} jogou? "))
    for c in range(0,6):
        partidas.append(int(input(f"    Quantos gols na partida {c}? ")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    times.append(jogador.copy())
    while True:
        resp = str(input("Quer continuar(S/N)? ")).upper()
        if resp in 'SN':
            break
        print("ERRO! Por favor responda S ou N.")
        if resp == 'N':
            break
print('-='*30)
for k, v in enumerate(times):
    print(f"{k}", end='')
    for d in v.values():
        print(f"{str(d)}", end='')
    print()
print('-='*30)
