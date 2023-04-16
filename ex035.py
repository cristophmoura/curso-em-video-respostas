r1 = input('Digite o comprimento da primeira reta: ')
r2 = input('Digite o comprimento da segunda reta: ')
r3 = input('Digite o comprimento da terceira reta: ')

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As medidas {}, {} e {} podem formar um triangulo :)' .format(r1, r2, r3))
else:
    print('Forma porra nenhuma isso ai')
