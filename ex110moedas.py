def dobro(n, s=False):
    v = n * 2
    if s:
        return moeda(v)
    else:
        return n * 2


def metade(n, s=False):
    v = n / 2
    if s:
        return moeda(v)
    else:
        return n / 2


def aumentar(n, p=0, s=False):
    v = n * (1 + (p / 100))
    if s:
        return moeda(v)
    else:
        return n * (1 + (p / 100))


def diminuir(n, p=0, s=False):
    v =  n * (1 - (p / 100))
    if s:
        return moeda(v)
    else:
        return n * (1 - (p / 100))


def moeda(a):
    return 'R${:.2f}'.format(a)


def resumo (a=0,b=0,c=0):
    print('-' * 30)
    print('{:>21}'.format('RESUMO DO VALOR'))
    print('-' * 30)
    print('{:<20} {}' .format('Preço analisado:', moeda(a)))
    print('{:<20} {}' .format('Dobro do preço:', moeda(dobro(a))))
    print('{:<20} {}'.format('Metade do preço:', moeda(metade(a))))
    print('{}{:<18} {}'.format(b,'% de aumento:', moeda(aumentar(a,b))))
    print('{}{:<18} {}'.format(c, '% de redução:', moeda(diminuir(a, c))))
    print('-' * 30)