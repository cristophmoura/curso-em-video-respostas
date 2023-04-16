def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def aumentar(n, p=0):
    return n * (1 + (p / 100))


def diminuir(n, p=0):
    return n * (1 - (p / 100))


def moeda(a):
    return 'R${:.2f}'.format(a)
