pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = (2023-int(input('Ano de Nascimento')))
pessoa['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['CTPS'] != 0:
    pessoa['contratacao'] = int(input('Ano de contratacao: '))
    pessoa['salario'] = float(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['idade']+(35-(2023-pessoa['contratacao']))
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')