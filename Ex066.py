num = soma = dig = 0
while True:
    num = int(input("Digite um número inteiro[999 para parar]: "))
    if num == 999:
        break
    soma += num
    dig += 1
print(f"A soma vale {soma}.")
print(f"A quantidade de numeros digitados foi {dig}.")
