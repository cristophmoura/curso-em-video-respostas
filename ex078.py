valores = []
cont = maior = menor = 0
while cont <= 5:
    valores.append(int(input(f'Digite um valor para a posicao {cont}')))
    if cont == 0:
        maior = menor = valores[0]
    if maior < valores[cont]:
        maior = valores[cont]
    if menor > valores[cont]:
        menor = valores[cont]
    cont += 1
print(valores)
print(f'O maior valor digitado foi {maior} nas posicoes ', end='')
for valor in range(len(valores)):
    if maior == valores[valor]:
        print(f'{valor}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posicoes ' ,end='')
for valor in range(len(valores)):
    if menor == valores[valor]:
        print(f'{valor}... ', end='')