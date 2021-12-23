nome = str(input("Digite seu nome:")).strip()

if nome[:5].upper() == 'SILVA':
    print("Que legal, você possui o nome Silva!")
else:
    print("Você não possui o nome Silva :(")