#Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:
#Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
#Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
#Não tem direito a voto (menor de 16 anos).
def voto(idade):
    if idade <= 0:
        return"Idade inválida."
    elif 70 > idade >= 18:
        return"Seu voto é obrigatório."
    elif 18 > idade >= 16 or idade >= 70:
        return"Você não é obrigado a votar."
    elif idade < 16:
        return"Você não é obrigado a votar"


idad = int(input("Qual sua idade? "))
print(voto(idad))