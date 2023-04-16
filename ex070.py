preco = precoMaisBarato = total = contProduto = cont = 0
produto = produtoMaisBarato = ''
continuar = 'S'

while continuar == 'S':
    cont += 1
    produto = input('Qual o nome? ')
    preco = float(input('Qual o preço? '))
    total += preco
    if cont == 1:
        precoMaisBarato = preco
    if preco > 1000:
        contProduto += 1
    if preco < precoMaisBarato:
        produtoMaisBarato = produto

    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
print(f'O total gasto foi: R${total}')
print(f'{contProduto} produtos custam mais que R$1000')
print(f'{produtoMaisBarato} é o produto mais barato')


