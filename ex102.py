def fat(n, show):
    """-> Calcula o fatorial de um número
    :param num: O número que ira ser calculado o fatorial
    :param show: (Opcional) Detalhes a mais do calculo do fatorial
    :return: O valor do fatorial do número passado..."""
    fatorial = 1
    if show == False:
        for c in range(1, n + 1):
            fatorial *= c
        print(fatorial)
    else:
        for c in range(1, n + 1):
            fatorial *= c
            if c == 1:
                print(f'{c} ', end='')
            else:
                print(f'x {c} ', end='')
        print(f'= {fatorial}')


# fat(int(input('Digita um número ae: ')))
num = int(input('Digita um número ae: '))
fat(num, True)
help(fat)