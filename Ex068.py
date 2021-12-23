from random import randint
resp = 'S'
while True:
    num = int(input("Digite um numero: "))
    tipo = ' '
    computador = randint(1, 11)
    total = num + computador
    while tipo not in 'PpIi':
        tipo = str(input("Par ou Impar?(P/I): ")).strip().upper()
    print(f"Você jogou {num} e o computador {computador}.Total de {total}.")
    if tipo == 'P':
        if total % 2 == 0:
            print("Você venceu!")
        else:
            print("Você perdeu!")
    elif tipo == 'I':
        if total % 2 == 1:
            print("Você venceu!")
        else:
            print("Você perdeu!")
    resp = str(input("Quer continuar?(S/N): ")).strip().upper()
    if resp == 'N':
        break