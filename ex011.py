altura = float(input('Qual a altura da parede? '))
largura = float(input('E a largura? '))
areaq = float(altura*largura)
tinta = float(areaq/2)
print('A parede tem uma area de {} e precisa de {} litros de tinta' .format(areaq, tinta))