from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1,8):
    nasc = int(input("Digite o ano de nascimento: "))
    idade = atual - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f"Ao todo tivemos {maior} pessoas de maioridade.")
print(f"Ao todo tivemos {menor} pessoas de menor de idade.")