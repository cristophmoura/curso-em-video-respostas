soma = cont = cond = 0
while cond != 999:
    n1 = int(input('Digite um numero: '))
    if n1 == 999:
        break
    soma += n1
    cont += 1
print(f'{soma}, {cont}')
