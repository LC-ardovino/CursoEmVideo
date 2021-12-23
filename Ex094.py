galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Digite um nome: "))
    while True:
        pessoa['sexo'] = str(input("Digite o sexo (M/F): ")).upper()
        if pessoa['sexo'] in 'MF':
            break
        elif pessoa['sexo'] != 'MF':
            print("ERRO! Por favor digite um valor válido.")
    pessoa['idade'] = int(input("Digite a idade:"))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar (S/N)?")).upper()
        if resp in 'SN':
            break
        print("Responda apenas S ou N.")
    if resp == 'N':
        break
print("-="*30)
print(f"Ao todo temos {len(galera)} pessoas.")
media = soma/len(galera)
print(f"A média das idades é {media}.")
print("As mulheres cadastradas foram ", end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f"{p['nome']}", end='')
print()
print('D) Lista das pessoas que estão acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f"{k} = {v}; ", end='')
        print()
print("<<< ENCERRADO >>>")

