numeros = []
pares =[]
impares = []
cont = 0
for numero in range(0,7):
    cont += 1
    numeros.append(int(input(f'Digite o {cont}o. valor: ')))
    if numeros[numero] % 2 == 0:
        pares.append(numeros[numero])
    else:
        impares.append(numeros[numero])
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
print(f'A lista completa em ordem crescente é: {sorted(numeros)}')
