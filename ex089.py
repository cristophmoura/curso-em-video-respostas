turma = []
aluno = []
notas = []
continuar = 'S'
cont = media = nota1 = nota2 = 0
while continuar == 'S':
    aluno.append(input('Nome: '))
    notas.append(input('Nota 1: '))
    notas.append(input('Nota 2: '))
    aluno.append(notas[:])
    turma.append(aluno[:])
    notas.clear()
    aluno.clear()
    continuar = input('Quer continuar? [S/N]').strip().upper()[0]

for i in turma:
    print(f'{cont:<4} {turma[cont][0]:<10} ',end='')
    nota1 = int(turma[cont][1][0])
    nota2 = int(turma[cont][1][1])
    media = (nota1+nota2)/2
    print(f'{media:>8}')
    cont+=1
