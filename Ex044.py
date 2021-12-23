compra = float(input("Digite o preço da compra: "))
print('''Escolha uma das formas de PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] em até 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input("Digite a opção: "))

if opcao == 1:
    print(f"O valor final da compra será:{(compra*90/100)}")
elif opcao == 2:
    print(f"A vista no cartão o valor será:{(compra*95/100)}")
elif opcao == 3:
    print(f"Em até 2X no cartão o valor final da conta será: {compra/2} por mês.")
elif opcao == 4:
    print(f"O valor final da conta em 3x ou mais no cartão será:{(compra/3)*1.2}")