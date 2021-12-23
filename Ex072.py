   #Crie um programa que tenha uma dupla totalmente preenchida com uma
# contagem por extenso, de zero até vinte. Seu programa deverá ler um
# número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20')


while True:
    pergunta = int(input("Digite um número entre 0 e 20: "))
    if 0<=pergunta<20:
        break
    print("Tente novamente.", end='')
print(f"O número digitado foi {numeros[pergunta]}")