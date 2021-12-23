#Exercício Python 078: Faça um programa que leia 5 valores numéricos
# e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.
valores = []

for c in range(0, 5):
     valores.append(int(input("Digite um número inteiro:")))
     maior = max(valores)
     menor = min(valores)
print(f"O maior valor é {maior} na(s) posições:")
for i,v in enumerate(valores):
    if v == maior:
        print(f"{i+1}...",end='')
print(f"\nO menor valor é {menor} na(s) posições:")
for i,v in enumerate(valores):
    if v == menor:
        print(f"{i+1}...",end='')
#print(f"O menor valor é {menor} e sua posição é {c}")
