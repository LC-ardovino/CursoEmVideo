
def conta(pess, final,divis ):

    print("----" * 15)
    print(f"O valor total da conta, com a taxa de serviço será de R$ {round(final, 1)}.")
    print(f"Dividindo a conta por {pess} pessoa(s), cada pessoa deverá pagar R$ {round(divis, 1)}.")
    print("----" * 15)

#Programa principal


pes = int(input("Digite o número de pessoas:"))
if pes <= 0:
    print("Informação inválida.")
    exit()
cons = float(input("Informe o valor total de consumo:R$ "))
percent = int(input("Informe o percentual do serviço, entre 0% e 100%: "))
if percent < 0 or percent > 100:
    print ("Percentual inválida.")
    exit()
consumo_final = ((cons*percent)/100+cons)
divisao = consumo_final/pes
conta(pes,consumo_final,divisao)



