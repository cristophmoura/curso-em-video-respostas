import datetime
ano = int(input('Qual o ano de nascimento? '))
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = int(date.strftime("%Y"))

if year - ano <= 9:
    print('Mirim')
elif year - ano > 9 and  year - ano <= 14:
    print('Infantil')
elif year - ano > 14 and year - ano <= 19:
    print('Junior')
elif year - ano > 19 and year - ano <= 20:
    print('Senior')
elif year - ano > 20:
    print('Master')
else:
    print('Não entendi')

