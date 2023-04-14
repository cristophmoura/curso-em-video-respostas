listagem = ('Pão',1,'Leite',3.50,'Frango',10.90)
print('-'*38)
print(f'{"Listagem de preço:":^40}')
print('-'*38)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>6.2f}')
print('-'*38)