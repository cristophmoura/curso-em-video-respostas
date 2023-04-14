matriz = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
res = pares = maior = maiorLinha = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range (0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
maior = matriz[0][0]
pares = 0
for l in range (0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
for l in range (0,3):
    res += matriz[l][2]

for c in range (0,3):
    if c == 0:
        maiorLinha = matriz[1][0]
    elif matriz [1][c] > maiorLinha:
        maiorLinha = matriz [1][c]

print(f'A soma de todos pares é {pares}')
print(f'A soma da terceira coluna é {res}')
print(f'O maior valor da segunda linha é {maiorLinha}')

