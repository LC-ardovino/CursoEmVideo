def contador(inicio, fim, passo):
    for num in range(inicio, fim, passo):
        print(num, end=' ')



print("Segue a contagem de 1 até 10, de 1 em 1:")
contador(1,11, 1)
print()
print('-'*30)
print("Segue a contagem de 10 até 0, de 2 em 2:")
contador(10,-1,-2)
print()
print('-'*30)
ini = int(input("Digite o início da contagem:"))
fim = int(input("Digite o fim da contagem:"))
pas = int(input("Digite os passos entre um número e outro: "))
if pas>0:
    contador(ini, fim+1, pas)
else:
    contador(ini, fim-1, pas)