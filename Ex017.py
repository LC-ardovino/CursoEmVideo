import math

cat = float(input("Digite o comprimento do cateto: "))
hip = float(input("Digite o comprimento da hipotenuza: "))
soma = (cat**2 + hip**2)

print(f"O valor da hipotenuza é {round(math.sqrt(soma),2)}")