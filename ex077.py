palavras = ('aprender', 'programar', 'zeladora', 'abajur')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ' , end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra , end=' ')







"""" 
   for palavra in tupla:
    print(f'Na palavra {palavra} temos: ',end='')
    tupla[palavra].count('a')

   
   
   
   
   if 'a' in palavra:
        print('A ')
    if 'b' in palavra:
        print(f'B ')"""