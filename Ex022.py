nome = str(input("Digite seu nome: ")).strip()


print(f"Seu nome em maiúsculo é {nome.upper()}")
print(f"Seu nome em minúsculo é {nome.lower()}")
print(f"O número de letras do seu nome é {len(nome)-nome.count(' ')}")
print(f"O seu primeiro nome tem ao todo {nome.find(' ')} letras")
#separa = nome.split()
#print(f"O numero de letras do seu primeiro nome é {len(separa[0])}")