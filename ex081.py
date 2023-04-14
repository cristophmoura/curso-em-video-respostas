valores = []
continua = 'S'
cont = 0

while continua == 'S':
    valores.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso...')
    cont += 1
    continua = input('Quer continuar? [S/N] ').strip().upper()[0]
print(f'Voce digitou {cont} valores')
print(f'Em ordem decrescente {sorted(valores, reverse=True)}')
pos = 0
while pos < len(valores):
    if 5 in valores:
        print('Tem 5 na lista')
    else:
        print('Não tem 5 na lista')
    pos += 1