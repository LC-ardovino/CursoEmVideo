#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão
# exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
resposta = 'S'

while True:
    n = int(input("Digite um número: "))
    if n not in valores:
        valores.append(n)
    else:
        print("Digite um número que não consta na lista.")
    resp = str(input("Quer continuar(S/N)?")).upper()
    if resp != resposta:
        print("Obrigado por usar nosso programa!")
        break
valores.sort()
print(f"Os valores adicionados foram {valores}.")