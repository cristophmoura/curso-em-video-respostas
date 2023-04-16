lista = []
listaPar = []
listaImpar = []
cont = 0
continua = 'S'

while continua == 'S':
    lista.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso...')
    continua = input('Quer continuar? [S/N] ').strip().upper()[0]
print(f'Voce digitou os valores {lista}')
for pos in range(0,len(lista)):
    if lista[pos] % 2 == 0:
        listaPar.append(lista[pos])
    else:
        listaImpar.append(lista[pos])
print(listaPar)
print(listaImpar)
