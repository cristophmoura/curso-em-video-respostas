idade = contIdade = cont = contM = contF = 0
genero = ''
continuar = 'S'

while continuar == 'S':
    idade = int(input('Qual a idade? '))
    genero = input('Qual gênero? [M/F]').strip().upper()[0]
    cont += 1
    if idade > 18:
        contIdade += 1
    if genero == 'M':
        contM += 1
    if genero == 'F' and idade < 20:
        contF += 1
    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
print(f'{contIdade} pessoas tem mais de 18 anos')
print(f'{contM} homens foram cadastrados')
print(f'{contF} mulheres tem menos de 20 anos')
