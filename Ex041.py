from datetime import date
atual = date.today().year
ano = int(input("Digite o ano de nascimento:"))
idade = atual-ano
if  idade>0 and idade<=9:
    print("Sua categoria é MIRIM.")
elif idade<0:
    print("Digite uma idade válida.")
elif idade>9 and idade<=14:
    print("Sua categoria é INFANTIL.")
elif idade>14 and idade<=19:
    print("Sua categoria é JÚNIOR.")
elif idade>19 and idade<=25:
    print("Sua categoria é Sênior.")
else:
    print("Sua categoria é MASTER.")