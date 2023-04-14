dic = dict()
dic['nome'] = str(input('Nome: '))
dic['media'] = float(input('Media: '))
if dic['media'] >= 6:
    dic['situacao'] = 'Aprovado'
else:
    dic['situacao'] = 'Reprovado'

print(f'O nome é: {dic["nome"]}')
print(f'A média é: {dic["media"]}')
print(f'A situação é: {dic["situacao"]}')
print('=-' *30)
# Usando FOR

for k, v in dic.items():
    print((f'{k} é igual a {v}'))