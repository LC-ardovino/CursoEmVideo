#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma
#tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor
#que estão na tupla.
from random import randint

n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram:{n[0]},{n[1]},{n[2]},{n[3]},{n[4]}. ')
print(f"O maior valor sorteado foi {max(n)}.")
print(f"O menor valor sorteado foi {min(n)}.")

