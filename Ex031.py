KM = float(input("Digite a distância desejada: "))
preço1 = round(KM * 0.5, 2)
preço2 = round(KM * 0.45, 2)
if KM <= 200:
    print(f"O preço cobrado será {preço1}.")
else:
    print(f"O preço cobrado será {preço2}.")