valor = float(input("Qual o valor da casa desejada? "))
salario = float(input("Qual seu salário? "))
meses = int(input("Em quantos meses você quer parcelar? "))
porcentagem = round((salario*30)/100, 2)
preco_mensal = round(valor/meses, 2)

if preco_mensal>porcentagem:
    print("Você não conseguiu o parcelamento.")
else:
    print(f"Parabéns! Sua nova casa será parcelada em {meses}X de {preco_mensal}.")