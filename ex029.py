velo = int(input('Qual a velocidade da caranga? '))
print('Tá safe' if velo <= 80 else 'MULTADO! Você tem que pagar {} mangos' .format((velo-80)*7))