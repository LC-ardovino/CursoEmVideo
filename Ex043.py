peso = float(input("Informe seu peso: "))
altura = float(input("Informe a sua altura: "))
IMC = round(peso/altura**2, 2)

if IMC < 18.5:
    print("Abaixo do Peso normal.")
elif  25>=IMC>18.5:
    print("Peso Ideal.")
elif  30>=IMC>25:
    print("Sobrepeso.")
elif  40>=IMC>30:
    print("Obesidade.")
else:
    print("Obesidade Mórbita.")