def notas(total, MAX, MIN, MEDIA):
    r = dict()
    r['Total:'] = total
    r['MAX:'] = MAX
    r['MIN:'] =MIN
    r['MÉDIA:'] =MEDIA
    if media >= 7:
        print("Sua situação é boa.")
    elif media >= 5:
        print("Razoável.")
    else:
        print("Situação crítica.")
    return r


#PROGRAMA PRINCIPAL
total = list()
numero_de_alunos = int(input("Digite o número de alunos: "))
for n in range(1, numero_de_alunos+1):
    nota = int(input(f"Digite a nota do {n} aluno:"))
    total.append(nota)
    tot = len(total)
    maximo = max(total)
    minimo = min(total)
    media = sum(total)/tot

print(notas(tot, maximo, minimo, media))

