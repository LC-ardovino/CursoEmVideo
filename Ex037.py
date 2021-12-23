num = int(input("Digite um número: "))
print('''Escolha uma das bases para conversão:
[1] para binário.
[2] para octal
[3] para hexadecimal''')

opcao = int(input("Sua opção: "))

if opcao == 1:
    print(f"O numero {num} convertido para binário é {bin(num) [2:]}")
elif opcao == 2:
    print(f"O numero {num} convertido para octal é {oct(num) [2:]}")
elif opcao == 3:
    print(f"O numero {num} convertido para hexa é {hex(num) [2:]}")
else:
    print("Valor invalido, tente novamente.")