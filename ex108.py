import ex108moedas

p = float(input('Digite o preço em R$ '))
print(f'A metade de {ex108moedas.moeda(p)} é {ex108moedas.moeda(ex108moedas.metade(p))}')
print(f'O dobro de {ex108moedas.moeda(p)} é {ex108moedas.moeda(ex108moedas.dobro(p))}')
print(f'Aumentando 10%, temos {ex108moedas.moeda(ex108moedas.aumentar(n=p, p=10))}')
print(f'Reduzindo 13%, temos {ex108moedas.moeda(ex108moedas.diminuir(n=p, p=13))}')