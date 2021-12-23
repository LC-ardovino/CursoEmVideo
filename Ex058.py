from random import randrange
num = randrange(0,10)
sort = input("Digite um numero entre 0 e 11: ")
tentativa = 1
acertou = False
while not acertou:
    jogador = int(input("Qual é seu palpite?"))
    tentativa += 1
    if jogador == num:
        acertou = True
print("Acertou!")
print(f"O numero de tentativas foi {tentativa}.")

