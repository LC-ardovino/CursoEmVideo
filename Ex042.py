c1 = int(input("Digite o primeiro comprimento:"))
c2 = int(input("Digite o segundo comprimento:"))
c3 = int(input("Digite o terceiro comprimento:"))
existe = c1<c2+c3 and c2<c1+c3 and c3<c1+c2
equilatero = c1==c2==c3
isosceles = c1==c2 or c2==c3 or c3==c1
escaleno = c1!=c2!=c3

if existe and equilatero is True:
    print("O triangulo é equilatero.")
elif existe and isosceles is True:
    print("O triangulo é isósceles!")
elif existe and equilatero is True:
    print("O triangulo é escaleno.")

else:
    print("Infelizmente ele não existe.")