n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um: '))
if n1 > n2:
    print('{} é o maior e o {} é menor' .format(n1, n2))
elif n1 < n2:
    print('{} é menor e o {} é maior' .format(n1,n2))
else:
    print('Os números são iguais')