#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = []
while True:
    n = int(input("Digite um valor inteiro: "))
    lista.append(n)
    resp = str(input("Quer continuar(S/N)?"))
    if resp in 'Nn':
        print("Obrigado por usar nossos serviços, segue a lista criada....")
        break
if 5 in lista:
    print("O número 5 está na lista.")
else:
    print("O número 5 não está na lista.")
lista.sort(reverse=True)
print(f"A lista criada foi {lista}.")
print(f"O número de valores digitados foi {len(lista)}.")
