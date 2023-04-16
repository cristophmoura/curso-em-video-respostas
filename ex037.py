n1 = int(input('Digita um número inteiro: '))
base = int(input('Quer converter para o que?\n1. binário\n2. octal\n3. hexa\nQuero converter para: '))
if base == 1:
        print('{} em binário é: {}' .format(n1, bin(n1)))
elif base == 2:
    print('{} em octal é: {}'.format(n1, oct(n1)))
elif base == 3:
    print('{} em hexadecimal é: {}'.format(n1, hex(n1)))
else:
    print('É de 1 a 3 sua anta')
