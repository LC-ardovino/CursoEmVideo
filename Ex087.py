matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scot = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor de [{l},{c}]:"))
print("-="*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]}]", end='')
        if matriz[l][c] % 2 ==0:
            spar += matriz[l][c]
    print()
print("-="*30)
print(f"A soma dos valores pares vale {spar}.")
for l in range(0,3):
    scot += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {scot}.")
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f"O maior valor da segunda linha é {mai}")