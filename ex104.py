def leiaInt():
    n = input('Digite um numero inteiro: ')
    while True:
        if n.isnumeric():
            n = int(n)
            if isinstance(n, int):
                return n
                break
        else:
            print('ERRO!')
            n = input('Digite um numero inteiro: ')


print(f'Você digitou o número {leiaInt()}')

