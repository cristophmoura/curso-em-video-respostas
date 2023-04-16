import time
def contador(a,b,c):
    linha()
    if a > b:
        if c == 0:
            print(f'    Contagem de {a} até {b} de 1 em 1')
            for i in range(b,a+1):
                print(f' {a}', end='')
                a -= 1
                time.sleep(0.3)
        else:
            print(f'    Contagem de {a} até {b} de {c} em {c}')
            for i in range(a, b-1, c):
                print(f' {a}', end='')
                a += c
                time.sleep(0.3)
    elif a < b:
        if c == 0:
            print(f'    Contagem de {a} até {b} de 1 em 1')
            for i in range(a, b + 1):
                print(f' {a}', end='')
                a += 1
                time.sleep(0.3)
        else:
            print(f'    Contagem de {a} até {b} de {c} em {c}')
            for i in range(a, b + 1, c):
                print(f' {a}', end='')
                a += c
                time.sleep(0.3)
    print(' FIM!')


def linha():
    print('~' * 39)
    print('~' * 39)


cont = 0
num = 0
linha()
for i in range(0, 10):
    print(f'  {num}', end='')
    num += 1
    time.sleep(0.3)
print('  FIM!')
linha()
num = 10
for i in range(0, 5):
    print(f'    {num}', end='')
    num -= 2
    time.sleep(0.3)
print('    FIM!')
linha()
print('     Agora é a sua vez meu chapa')
inicio = fim = contagem = 0


inicio = int(input('Início: '))
fim = int(input('Fim: '))

while True:
    contagem = int(input('Contagem: '))
    if inicio < fim and contagem >= 0:
        break
    elif inicio > fim and contagem <= 0:
        break
    print(f'Voce pediu para começar em {inicio} e terminar em {fim}.\nA contagem de {contagem} em {contagem} está errada.')
contador(inicio,fim,contagem)
