import ex109moedas

p = float(input('Digite o preço em R$ '))
print(f'A metade de {ex109moedas.moeda(p)} é {ex109moedas.metade(p, True)}')
print(f'O dobro de {ex109moedas.moeda(p)} é {ex109moedas.dobro(p, True)}')
print(f'Aumentando 10%, temos {ex109moedas.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {ex109moedas.diminuir(p, 13, False)}')
