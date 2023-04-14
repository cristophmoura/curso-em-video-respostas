valores = []
continua = 'S'
cont = 0

while continua == 'S':
    valores.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso...')
    continua = input('Quer continuar? [S/N] ').strip().upper()[0]
print(f'Voce digitou os valores {valores}')