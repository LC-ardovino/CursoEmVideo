soma = 0
maioridadehomem = 0
nomevelho = ''
totmulher = 0
for pess in range(1,5):
    print("-----------------------------")
    nome = str(input(f"Digite o nome da {pess} pessoa:"))
    sexo = str(input(f"Qual o sexo(H/M) da {pess} pessoa?"))
    idade = int(input(f"Digite a idade da {pess} pessoa:"))
    if idade > 0:
        soma += idade
    if pess == 1 and sexo in 'Hh':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Hh' and idade>maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade<20:
        totmulher += 1
media = soma/4
print(f"A média das idades é {media} anos.")
print(f"O homem mais velho tem {maioridadehomem} anos.")
print(f"O nome do homem mais velho é {nomevelho}.")
