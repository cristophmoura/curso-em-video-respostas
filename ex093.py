dic = dict()
gols = list()
tudo = 0
dic['nome'] = str(input('Nome do Jogador: '))
dic['partidas'] = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
for i in range(0,dic['partidas']):
    gols.append(int(input(f'Quantos gols na partida {i}?')))
    tudo += gols[i]
dic['gols'] = gols
dic['total'] = tudo
print('=-' *30)
print(dic)
print('=-' *30)
for k, v in dic.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-' *30)
print(f'O jogador {dic["nome"]} jogou {dic["partidas"]} partidas')
for i, v in enumerate(gols):
    print(f'  => Na partida {i}, fez {v} gols')
print(f'Foi um total de {dic["total"]} gols')
