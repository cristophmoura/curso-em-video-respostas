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

