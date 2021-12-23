#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo
#teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
from random import randint
n = (int(input("Digite um número: "))
    ,int(input("Digite um número: "))
    ,int(input("Digite um número: "))
    ,int(input("Digite um número: ")))
if 3 in n:
    print(f"O número 3 está na posição {n.index(3)+1}")
else:
    print("O número 3 não foi digitado.")
if 9 in n:
    print(f"O número nove apareceu {n.count(9)}")
else:
    print("O número 9 não pôde ser contabilizado")
for num in n:
    if num % 2 == 0:
        print(num, end=' ')