import random
import time
valores = list()
def sorteio():
    valor = 0
    print(f'Gerando os valores: ' ,end='')
    for i in range(0,5):
        valor = random.randint(0,10)
        print(f'{valor} ' ,end='')
        time.sleep(0.3)
        valores.append(valor)
    print('PRONTO!')
def soma(a):
    total = 0
    cont = 0
    for i in valores:
        if valores[cont] % 2 == 0:
            total += valores[cont]
        cont += 1
    print(f'Somando os valores PARES de {valores}, temos {total}')

sorteio()
soma(valores)


