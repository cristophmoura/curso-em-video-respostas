grupo = list()
pessoa = dict()
media = soma = cont = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['genero'] = str(input('Genero: ')).strip().upper()[0]
        if pessoa['genero'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    grupo.append(pessoa.copy())
    while True:
        continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas')
for i in grupo:
    soma += grupo[cont]['idade']
    cont+= 1
media = soma/len(grupo)
print(f'B) A média de idade é de {media:5.2f} anos.')
cont = 0
print(f'C) As mulheres cadastradas foram:' ,end='')
for i in grupo:
    if grupo[cont]['genero'] == 'F':
        print(f' {grupo[cont]["nome"]}', end='')
    cont += 1
print()
print(f'D) Lista das pessoas que estao acima da media')
cont = 0
for i in grupo:
    if grupo[cont]['idade'] >= media:
        print(f'nome = {grupo[cont]["nome"]}; genero = {grupo[cont]["genero"]}; idade = {grupo[cont]["idade"]}')
        cont+=1





"""" 
=-=-=-=- USANDO APENAS LISTAS (primeira tentativa) =-=-=-=-=-

grupo = list()
pessoa = list()
continuar = 'S'
soma = cont = 0
while continuar == 'S':
    pessoa.append(str(input('Nome: ')))
    pessoa.append(str(input('Genero: ')).strip().upper()[0])
    pessoa.append(int(input('Idade: ')))
    grupo.append(pessoa[:])
    pessoa.clear()
    cont += 1
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
print(f'O grupo tem {cont} pessoas.')
print(f'As mulheres cadastradas foram:' ,end='')
cont = 0
for i in grupo:
    soma += grupo[cont][2]
    if grupo[cont][1] == 'F':
        print(f' {grupo[cont][0]}', end='')
    cont +=1
media = soma/cont
print()
print(f'A média de idade é de {media} anos')
cont = 0
print(f'Lista das pessoas que estao acima da media: ')
for i in grupo:
    if grupo[cont][2] > media:
        print(f'nome = {grupo[cont][0]}; genero = {grupo[cont][1]}; idade = {grupo[cont][2]}')
    cont+=1
"""