import random
numeros_aleatorios = tuple(random.sample(range(1, 101), 5))
menor = maior = cont = 0
for numero in numeros_aleatorios:
    if cont == 0:
        menor = maior = numeros_aleatorios[0]
    if numeros_aleatorios[cont] > maior:
        maior = numeros_aleatorios[cont]
    if numeros_aleatorios[cont] < menor:
        menor = numeros_aleatorios[cont]
    cont += 1
print(maior, menor)
print(f'Os números foram:',numeros_aleatorios)
