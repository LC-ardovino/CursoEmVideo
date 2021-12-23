aluno = dict()
aluno['Nome'] = str(input("Digite o nome: "))
aluno['Nota'] = float(input(f"A nota do aluno {aluno['Nome']}:"))
if aluno['média'] >= 7:
    aluno['Situação'] = 'Aprovado.'
elif 5 <= aluno['média'] < 7:
    aluno['Situação'] = 'Recuperação.'
else:
    aluno['Situação'] = 'Reprovado.'