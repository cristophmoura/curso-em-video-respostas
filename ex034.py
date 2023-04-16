sal = float(input('Qual teu salario maluco? R$'))
if sal >= 1250:
   novo_sal = sal*1.1
   print('Agora tu vai ganhar R${:.2f}' .format(novo_sal))
else:
    novo_sal = sal*1.15
    print('Vai começar a pingar R${:.2f}' .format(novo_sal))
