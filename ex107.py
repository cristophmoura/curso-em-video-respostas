import ex107moedas

p = float(input('Digite o preço em R$ '))
print(f'A metade de {p} é {ex107moedas.metade(p)}')
print(f'O dobro de {p} é {ex107moedas.dobro(p)}')
print(f'Aumentando 10%, temos {ex107moedas.aumentar(n=p, p=10)}')
print(f'Reduzindo 13%, temos {ex107moedas.diminuir(n=p, p=13)}')