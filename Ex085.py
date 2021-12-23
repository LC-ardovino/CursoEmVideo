numeros = [[], []]

for n in range(1,8):
    num = int(input(f"Digite o {n}o. valor: "))
    if num  % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print(f"A lista com os valores pares é {numeros[0]}")
print(f"A lista com os valores impares é {numeros[1]}")




