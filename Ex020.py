import random

aluno1 = str(input("Digite seu nome: "))
aluno2 = str(input("Digite seu nome: "))
aluno3 = str(input("Digite seu nome: "))
aluno4 = str(input("Digite seu nome: "))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print (f"A ordem dos escohidos é: {lista}" )
