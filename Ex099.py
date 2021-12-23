def maior(num):
    print(f"O maior número é {num}")


#programa principal
max = 0
while True:
    inteiro = int(input("Digite um numero inteiro: "))
    resp =str(input("Quer continuar (S/N)?")).upper()
    if resp in "Nn":
        break
    elif inteiro > max:
        max = inteiro

print(maior(max))
