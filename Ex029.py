veloc = float(input("Digite a velocidade do carro: "))
excedente = veloc-80
multa = round(excedente*7, 2)
if veloc >= 80:
    print(f"A multa será de {multa}$.")
else:
    print("A sua velocidade está dentro dos parâmetros.")