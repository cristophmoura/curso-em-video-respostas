pessoas = []
galera = []
continuar = 'S'
cont = maiorPeso = menorPeso = 0
pessoaMaiorPeso = []
pessoaMenorPeso = []
while continuar == 'S':
    pessoas.append(input('Nome: '))
    pessoas.append(input('Peso: '))
    galera.append(pessoas[:])
    pessoas.clear()
    cont += 1
    continuar = input('Quer continuar? [S/N]').strip().upper()[0]
maiorPeso = menorPeso = galera[0][1]
for pessoa in galera:
    if pessoa[1] >= maiorPeso:
        maiorPeso = pessoa[1]
    if pessoa[1] <= menorPeso:
        menorPeso = pessoa[1]
for pessoa in galera:
    if pessoa[1] == maiorPeso:
       pessoaMaiorPeso.append(pessoa[0])
    if pessoa[1] == menorPeso:
        pessoaMenorPeso.append(pessoa[0])

print(f'O maior peso foi de {maiorPeso}. Peso de {pessoaMaiorPeso}')
print(f'O menor peso foi de {menorPeso}. Peso de {pessoaMenorPeso}')
print(f'Foram cadastradas {cont} pessoas')
print(galera)
