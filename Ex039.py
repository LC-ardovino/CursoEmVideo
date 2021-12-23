idade = int(input("Digite a sua idade:"))
servico_militar = 18
atraso = idade-servico_militar

if idade==18:
    print("Está na hora de você se alistar no exercito!")
elif idade<18:
    print(f"Ainda não está na hora do seu alistamento...mas faltam {18-idade} anos.")
else:
    print(f"Já passou da hora de você se alistar,está atrasado a {atraso} anos.")