import time
def linha():
    print('-=' * 20)


def maior(* num):
    cont = maior = 0
    for i in range(0,len(num)):
        if cont == 0:
            maior = num[cont]
        elif maior < num[cont]:
            maior = num[cont]
        cont += 1
    linha()
    print('Analisando os valores passados...')
    cont = 0
    for i in range(0,len(num)):
        print(f'{num[cont]} ', end='')
        time.sleep(0.3)
        cont += 1
    print(f'Foram passados ao todo {cont} valores')
    print(f'O maior valor é {maior}')


maior(2,4,10,54,8,0)
maior(0)
maior(4,2)
maior(0,2,7,89,4,6,8,9,2)