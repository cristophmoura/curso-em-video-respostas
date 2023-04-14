casa = int(input('Qual o valor da casa? R$'))
sal = int(input('Quanto tu ganha? R$'))
anos = int(input('Quer meter em quantos anos? '))
mensal = casa / (anos * 12)

if mensal <= sal*0.30:
    print('A baia é tua malandro')
else:
    print('Vai dar não. A prestação mensal é {} e tá acima de 30% do teu salário de {} :/' .format(mensal, sal))
