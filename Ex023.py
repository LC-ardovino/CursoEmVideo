num = int(input("Digite um número inteiro de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"O numero {num} possui {u} unidades.")
print(f"O numero{num} possui {d} dezenas.")
print(f"O numero{num} possui {c} centenas.")
print(f"O numero{num} possui {m} milhares.")
