cidade = str(input("Digite o nome da cidade: ")).strip()
if (cidade[:5].upper() == 'SANTO' ):
    print("Você nasceu numa cidade com nome Santo!")
else:
    print("Você não nasceu numa cidade com nome Santo :(")