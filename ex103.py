def ficha(j='<Desconhecido>', g=0):
    print(f'O jogador {j} fez {g} gols.')


jogador = input('Qual nome do jogador? ')
gols = input('Qual o numero de gols? ')
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(g=gols)
else:
    ficha(jogador, gols)