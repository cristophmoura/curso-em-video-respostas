r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As medidas {:.0f}, {:.0f} e {:.0f} podem formar um triangulo ' .format(r1, r2, r3) , end='')
    if r1 == r2 == r3:
        print('equilátero.')
    elif r1 != r2 !=r3 !=r1:
        print('escaleno.')
    else:
        print('isósceles.')
else:
    print('Forma porra nenhuma isso ai')

