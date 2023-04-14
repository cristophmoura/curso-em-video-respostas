import datetime
ano = int(input('Qual o ano de nascimento? '))
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = int(date.strftime("%Y"))
idade = int(year - ano)
restante = 17 - idade
pos = idade - 17

if year - ano == 17:
    print('Vai se alistar pangaré')
elif year - ano < 17:
    print('Te livrou, ainda faltam {} anos p se alistar' .format(restante))
else:
    print('Tá veio já meu parcero, já passaram {} anos do alistamento' .format(pos))
