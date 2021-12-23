#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
# listas extras que vão conter apenas os valores pares e os valores ímpares
# digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

numeros = []
pares = []
impares = []

while True:
    n = int(input("Digite um número inteiro: "))
    numeros.append(n)
    resp = str(input("Quer continuar(S/N)?"))
    ultimo = numeros[-1]
    if resp in 'Nn':
        print("Obrigado por usar nossos serviços, segue a lista criada....")
        break
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 ==1:
        impares.append(n)
if ultimo % 2 == 0:
    pares.append(ultimo)
else:
    impares.append(ultimo)

print(numeros)
print(pares)
print(impares)