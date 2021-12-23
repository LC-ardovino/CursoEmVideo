#PROGRAMA PRINCIPAL


import moeda
valor = float(input("Digite o preço: R$"))
print(f"A metade do valor é R$ {moeda.metade(valor)}")
print(f"O dobro do valor é R$ {moeda.dobro(valor)}")
print(f"O valor somado em 10% é R$ {moeda.aumentar(valor)}")
print(f"O valor diminuido em 10% é R$ {moeda.diminuir(valor)}")