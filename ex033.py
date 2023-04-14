n1 = int(input('Digita o primeiro numero: '))
n2 = int(input('Digita o segundo numero: '))
n3 = int(input('Digita o terceiro numero: '))
if n1 > n2 and n1 > n3:
    print('O primeiro número é o maior {}' .format(n1))
else:
    if n2 > n1 and n2 > n3:
        print('O segundo número é o maior {}' .format(n2))
    else:
        print('O terceiro número é o maior {}' .format(n3))
if n1 < n2 and n1 < n3:
    print('O primeiro número é o menor {}' .format(n1))
else:
    if n2 < n1 and n2 < n3:
        print('O segundo número é o menor {}' .format(n2))
    else:
        print('O terceiro número é o menor {}' .format(n3))