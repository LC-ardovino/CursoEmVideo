c1 = int(input("Digite o primeiro comprimento:"))
c2 = int(input("Digite o segundo comprimento:"))
c3 = int(input("Digite o terceiro comprimento:"))
if c1<c2+c3 and c2<c1+c3 and c3<c1+c2:
    print("O triâgulo existe!")
else:
    print("Infelizmente ele não existe.")