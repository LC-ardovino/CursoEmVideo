N1 = float(input("Digite sua primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
media = round((N1+N2)/2, 1)

if media<5:
    print(f"Reprovado com média{media}.")
elif 5<=media<=6.9:
    print(f"Recuperação com média {media}.")
else:
    print(f"Parabéns! você tirou {media} e foi aprovado!")