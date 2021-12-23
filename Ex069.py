cont = 0
resp = 'S'
maiores = 0
menor = 0
mulher = 0
homem = 0
while True:
    print('-' * 20)
    sexo = str(input("Digite o seu sexo(H/M): ")).strip().upper()
    if sexo == 'H':
        homem += 1
    elif sexo == 'M':
        mulher += 1
    idade = int(input("Digite a sua idade: "))
    if idade > 18:
        maiores += 1
    if idade < 20 and sexo == 'M':
        menor += 1
    resp = str(input("Quer continuar?(S/N): ")).strip().upper()
    print('-' * 20)
    if resp == 'N':
        print(f"O número de homens é {homem}.")
        print(f"O número de mulheres é {mulher}.")
        print(f"O número de pessoas maiores que 18 é {maiores}.")
        print(f"O número de mulheres menores de 20 anos é {menor}.")
        break