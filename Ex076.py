#Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus
# respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

conteudo = ('Lápis', 2,
            'Video Game', 4000,
            'Computador', 15000,
            'Curso', 680,
            'Netflix', 30)
print('-'*40)
print(f'{"Listagem de Preços":.^40}')
print('-'*40)
for pos in range(0, len(conteudo)):
    if pos % 2 == 0:
        print(f'{conteudo[pos]:.<30}', end='')
    else:
        print(f'R${conteudo[pos]:>7.2f}')
print('-'*40)
