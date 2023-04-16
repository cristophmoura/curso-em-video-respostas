

def voto(ano):
    from datetime import date
    atual = date.today().year
    res = atual - ano
    if 70 >= res >= 18:
        return (f'Com {res} anos: Voto obrigatorio')
    elif res < 18:
        return (f'Com {res} anos: Não vota')
    else:
        return (f'Com {res} anos: É Opcional')

anoNascimento = int(input('Em que ano vc nasceu? '))
print(voto(anoNascimento))