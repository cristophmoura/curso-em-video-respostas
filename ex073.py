times = ('Atlético-MG', 'Internacional', 'São Paulo', 'Flamengo', 'Palmeiras', 'Santos', 'Grêmio', 'Fluminense', 'Ceará', 'Corinthians', 'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Sport', 'Fortaleza', 'Bahia', 'Vasco', 'Goiás', 'Botafogo', 'Coritiba')
cont = 0
print(' Os 5 primeiros colocados são:\n',times[:5])
print(' Os 4 últimos colocados são:\n',times[-4:])
print('Em ordem alfabética \n',sorted(times))
for pos, time in enumerate(times):
    cont += 1
    if time == 'Bahia':
        print(f'O Bahia está na ',cont,' posição do campeonato')