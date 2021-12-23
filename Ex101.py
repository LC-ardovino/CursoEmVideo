def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual-ano
    if idade <= 0:
        return"Idade inválida."
    elif 70 > idade >= 18:
        return"Seu voto é obrigatório."
    elif 18 > idade >= 16 or idade >= 70:
        return"Você não é obrigado a votar."
    elif idade < 16:
        return"Você não é obrigado a votar"


nasc = int(input("Em que ano você nasceu? "))
print(voto(nasc))