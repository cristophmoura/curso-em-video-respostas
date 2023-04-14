jogadores = []
dic = dict()
gols = list()
dic['total'] = cont = dados = qntJogadores = 0
resp = ''
while True:
    total = 0
## Inputs pro dicionario
    dic['nome'] = str(input('Nome do Jogador: '))
    dic['partidas'] = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    for i in range(0, dic['partidas']):
        gols.append(int(input(f'Quantos gols na partida {i}?')))
        total += gols[i]
    dic['gols'] = gols[:]
    gols.clear()
    dic['total'] = total
## Input do jogador pra lista
    jogadores.append(dic.copy())
## Quer repetir? (sim ou nao)
    while True:
        resp = str(input('Quer adicionar mais jogadores? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp == 'N':
        break
print('=-' *24)
print('{:<4} {:<15} {:<22} {:<1}'.format('cod', 'nome', 'gols', 'total'))
print('-' *48)
for i in jogadores:
    print('{:<4} {:<15} {:<22} {:<10}'.format(qntJogadores, jogadores[qntJogadores]["nome"], str(jogadores[qntJogadores]["gols"]), jogadores[qntJogadores]["total"]))
    qntJogadores += 1
print('-' *48)
## Mostrar dados de algum jogador
while True:
    dados = input('Mostrar dados de qual jogador? ')
    if dados.isdigit():
        dados = int(dados)
        if dados <= qntJogadores-1 and dados >= 0:
            break
        print('Este jogador nao existe')
    else:
        print('Voce precisa digitar um número')
print('-' *48)
print(f'Levantamento do jogador {jogadores[dados]["nome"].upper()}:')

for i, v in enumerate(jogadores):
    if i == dados:
        for i, v in enumerate(jogadores[dados]["gols"]):
            print(f'Na partida {i} fez {v} gols')






