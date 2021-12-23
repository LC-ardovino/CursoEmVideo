salario = float(input("Digite seu salário:"))
aumento1 = round((salario*110)/100, 2)
aumento2 = round((salario*115)/100, 2)
if salario > 1250:
    print(f"O seu aumento é de {aumento1}")
else:
    print(f"Seu aumento é de {aumento2}")