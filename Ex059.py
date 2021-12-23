num = float(input("Digite um número: "))
num1 = float(input("Digite outro número: "))
opçao = 0
while opçao != 5:
    print("""       [ 1 ] somar
       [ 2 ] multiplicar
       [ 3 ] maior
       [ 4 ] novos números
       [ 5 ] sair do programa""")
    opçao = int(input("Digite a sua opção: "))
    if opçao == 1:
        soma = num +num1
        print(round(soma))
    elif opçao == 2:
        mult = num*num1
        print(round(mult))
    elif opçao == 3 :
        if num>num1:
            print(num)
        else:
            print(num1)
    elif opçao == 4:
        print("Informe os numeros novamente.")
        num = int(input("Digite o priemiro número: "))
        num1 = int(input("Digite o segundo número: "))
    elif opçao == 5:
        print("Finalizando....")
    else:
        print("Digite uma opção válida: ")
print("Fim do programa....obrigado por usar nossos serviços.")