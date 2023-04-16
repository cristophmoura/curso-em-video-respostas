def res(* notas, sit=False):
    """-> Função para mostar os dados das notas de um determinado aluno
    :param notas: Notas do aluno
    :param sit: (Opcional) Mostar a situação do aluno
    :return: Retorna um dicionário com os dados das notas do aluno"""
    cont = maior = menor = total = 0
    boletim = {}
    for i in range(0, len(notas)):
        if i == 0:
            maior = menor = notas[0]
        elif notas[i] > maior:
            maior = notas[i]
        elif notas[i] < menor:
            menor = notas[i]
        total += notas[i]
        cont += 1
    media = total / cont
    boletim["total"] = cont
    boletim["maior"] = maior
    boletim["menor"] = menor
    boletim["media"] = media
    if sit == True:
        if media >= 7:
            boletim["situacao"] = 'BOA'
        elif media >= 6 and media <= 7:
            boletim["situacao"] = 'RAZOAVEL'
        else:
            boletim["situacao"] = 'RUIM'
    return(f'{boletim}')


resp = res(4.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(res)