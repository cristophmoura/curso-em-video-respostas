produto = 100
condi = int(input('O produto custa R$100. Qual a forma de pagamento?\n'
                  '[1] A vista \n'
                  '[2] A vista no cartão com 5% de desconto \n'
                  '[3] Em até 2x no cartão sem juros \n'
                  '[4] 3x ou mais no cartão com 20% de juros \n'
                  'Qual opção? '))
um = produto - produto*0.10
dois = produto - produto*0.05
quatro = produto*1.2
if condi == 1:
    print('A vista com desconto o valor fica R${}' .format(um))
elif condi == 2:
    print('A vista no cartão com 5% de desconto fica R${}' .format(dois))
elif condi == 3:
    print('Em até 2x no cartão o total fica {}' .format(produto))
elif condi == 4:
    print('3x ou mais no cartão fica R${}' .format(quatro))
else:
    print('É de 1 a 4 parcero')
