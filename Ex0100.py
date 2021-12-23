numeros = list()

from random import randint

def sortear(inicio, fim):
    for num in range(0, 5):
        n = randint(inicio, fim)
        numeros.append(n)
    print(f"A lista criada com o limite estabelecido foi: {numeros}")

def somaPar(numeros):
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f"A soma dos valores pares é {soma}")


#PROGRAMA PRINCIPAL
som = 0
print("--------Escolha o limite----------")
ini = int(input("Digite o inicio do sorteio: "))
end = int(input("Digite o fim do sorteio: "))
sortear(ini, end)
somaPar(numeros)


