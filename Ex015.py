dias = int(input("Quantos dias o carro percorreu? "))
KM = float(input("Quantos kilometros o carro percorreu? "))

preço_dia = (dias*60)
preço_KM = round((KM*0.15),2)
preço_final = (preço_KM+preço_dia)

print(f"O preço final de acordo com a quantidade de dias e de kilimetros percorridos é {preço_final}$.")