nome = str(input("Digite seu nome: ")).strip()

separa = nome.split()
primeiro_nome = separa[0]
ultimo_nome = separa[-1]

print(f"O primeiro nome do {nome} é {primeiro_nome}")
print(f"O ultimo nome do {nome} é {ultimo_nome}")