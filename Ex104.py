def leiaint(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("ERRO! Digite um valor válido.")
        if ok:
            break
    return valor


#PROGRAMA PRINCIPAL
n = leiaint("Digite um número:")
print(f"Você acabou de digitar o número {n}.")