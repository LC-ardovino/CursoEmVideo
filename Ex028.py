from random import randrange
num = randrange(0, 6)
sort = int(input("Digite um numero:"))

if num == sort:
    print("Parabéns! Você advinhou certo.")
else:
    print("Tente novamente")