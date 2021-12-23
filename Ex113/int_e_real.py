def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("Por favor digite um valor inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print("O usuário preferiu n digitar nenhum valor.")
            return 0
        else:
            return n


def leiafloat(msg2):
    while True:
        try:
            n = float(input(msg2))
        except (ValueError, TypeError):
            print("Por favor digite um valor Real válido.")
            continue
        except (KeyboardInterrupt):
            print("O usuário preferiu n digitar nenhum valor.")
            return 0
        else:
            return n
