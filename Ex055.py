menor = 0
maior = 0
for pess in range(1,6):
    peso = int(input(f"Digite o peso da {pess} pessoa:"))
    if pess == 1:
        maior=pess
        menor=pess
    else:
        if peso>maior:
            maior = peso
        elif peso<menor:
            menor = peso
print(f"O maior peso lido foi {maior}Kg")
print(f"O menor peso lido foi {menor}Kg")

