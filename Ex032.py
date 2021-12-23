ano = int(input("Digite um ano:"))
bi = ano % 4 == 0
if bi is True:
    print("É um ano bissexto!")
else:
    print("Infelizmente não é bissexto.")