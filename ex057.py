ex057

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Nao deu, informa o genero')).strip().upper()[0]
print(f" genero {sexo} registrado")