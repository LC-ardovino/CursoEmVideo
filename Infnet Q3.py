def concurso(notA, notA_vence, nom_vence):
    if notA < 0 or nota > 10 :
        print("Nota inválida.")
        exit()
    print(f"O vencedor teve nota igual a {notA_vence} e seu nome é {nom_vence}")




for n in range(1,6):
    nome = str(input(f"Digite o nome da(o) {n} participante: "))
    nota = float(input(f"Digite a nota da(o) {n} participante: "))
    if nota < 0 or nota > 10 :
        print("Nota inválida.")
        exit()
    if n == 1:
        nota_vencedor = nota
        nome_venc = nome
    elif nota > nota_vencedor:
        nota_vencedor = nota
        nome_venc = nome
concurso(nota,nota_vencedor, nome_venc)





