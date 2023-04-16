ano = int(input('Digita um ano ae: '))
if ano % 4 == 0 and ano % 100 > 0 or ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('É bisexto')
else:
    print('Não é bixesto não')

