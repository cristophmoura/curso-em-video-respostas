import random
sort = int(input('Quantos jogos que sortear? '))
megaSena = []
jogos = []
ultimoNumero = cont = 0

for j in range(0,sort):
    for jogo in range(0,6):
        if jogo == 0:
            jogos.append(random.randint(0, 60))
        else:
            ultimoNumero = random.randint(0, 60)
            if ultimoNumero not in jogos:
                jogos.append(random.randint(0, 60))
    megaSena.append(jogos[:])
    jogos.clear()
    print(f'Jogo {cont+1}: {sorted(megaSena[cont])}')
    cont += 1
