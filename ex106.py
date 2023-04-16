# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
def ajuda(hp):
    help(hp)
    print('\033[m')


print('='*30)
print(f'\033[32m{"SISTEMA DE AJUDA":^30}\033[m')
while True:
    print('=' * 30)
    print('Digite a palavra \033[31mFIM\033[m para acabar.')
    resp = input('Função ou Biblioteca -> ')
    print('=' * 30)
    print('\033[34m')
    if resp in 'FIM':
        break
    ajuda(resp)
