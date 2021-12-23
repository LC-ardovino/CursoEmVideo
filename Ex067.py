resp = 'S'
while True:
    num = int(input("Digite um número :"))
    print('-' * 10)
    if num < 0:
        print('Obrigado por utilizar nossa tabuada.')
        break
    else:
        for c in range(1, 11):
            print(f"{num} x {c} = {num*c}")
            print('-' * 10)
    resp = str(input("Quer continuar?(S/N): ")).strip().upper()
    if resp == 'N':
        print("Obrigado por utilizar nossa tabuada.")
        break