total = 0
resp = 'S'
caro = 0
menor = 0
cont = 0
while True:
    nome = str(input("Digite o nome do produto: "))
    preço = float(input("Digite o preço do produto: "))
    total += preço
    cont += 1
    if preço > 1000:
        caro += 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
    resp = str(input("Quer continuar?(S/N): ")).strip().upper()
    if resp == 'N':
        print(f"O total da compre é {total}$")
        print(f"O número de produtos que custam mais de 1000$ é {caro}.")
        print(f"O produto mais barato custa {menor}")
        break