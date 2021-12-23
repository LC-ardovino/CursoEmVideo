sexo = str(input("Informe seu sexo (H/M): ")).strip().upper()
while sexo not in 'HhMm':
    sexo =  str(input("Dado inválido, informe seu sexo novamente (H/M): ")).strip().upper()
print(f"Seu sexo é {sexo}!")

