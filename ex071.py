valor = int(input('Digite o valor a ser sacado: R$'))
cont100 = cont50 = cont20 = cont10 = cont1 = 0
while valor != 0:
    if valor > 100:
        cont100 += 1
        valor = valor - 100
    elif 100 > valor >= 50:
        cont50 += 1
        valor = valor - 50
    elif 50 > valor >= 20:
        cont20 += 1
        valor = valor - 20
    elif 20 > valor >= 10:
        cont10 += 1
        valor = valor - 10
    elif 10 > valor >= 1:
        cont1 += 1
        valor = valor - 1
print(f'{cont100} Notas de R$100\n{cont50} Notas de R$50\n{cont20} Notas de R$10\n{cont10} Notas de R$10\n{cont1} Notas de R$1')
