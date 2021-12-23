#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

dado_pessoa = []
dados_geral = []
mai = men = 0
while True:
    nome = str(input("Digite seu nome: "))
    peso = int(input("Digite seu peso: "))
    dado_pessoa.append(nome)
    dado_pessoa.append(peso)
    if len(dados_geral) == 0:
        mai = men = dado_pessoa[1]
    else:
        if dado_pessoa[1] > mai:
            mai = dado_pessoa[1]
        if dado_pessoa[1] < men:
            men = dado_pessoa[1]

    dados_geral.append(dado_pessoa[:])
    dado_pessoa.clear()
    resp = str(input("Quer continuar?(S/N) "))
    if resp in 'Nn':
        print("Obrigado por usar nossos serviços!")
        break
print(dados_geral)
print(f"Ao todo você cadastrou {len(dados_geral)} pessoas.")
print(f"O maior peso foi de {mai}KG do ", end="")
for p in dados_geral:
    if p[1] == mai:
        print(f"{p[0]}\n", end= "")
print(f"O menor peso foi de {men}KG do ", end='')
for p in dados_geral:
    if p[1] == men:
        print(f"{p[0]}", end = "")