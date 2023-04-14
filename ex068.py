import random

n1 = n2 = res = escolha = cont = 0
status = True
while status == True:
    n1 = int(input('Digita um número: '))
    escolha = input('Par ou impar? [P/I]: ').strip().upper()[0]
    n2 = random.randint(0, 11)
    res = (n1+n2) % 2
    if escolha == 'P':
        if res == 0:
            print(f'Voce ganhou! O pc escolheu {n2}. {n1} + {n2} = Par. Vamos até perder.')
            cont += 1
        else:
            print(f'Perdeu malandro, o pc escolheu {n2}. {n1} + {n2} = Ímpar filhao')
            status = False
    elif escolha == 'I':
        if res != 0:
            print(f'Voce ganhou! O pc escolheu {n2}. {n1} + {n2} = ímpar. Vamos até perder.')
            cont += 1
        else:
            print(f'Perdeu malandro, o pc escolheu {n2}. {n1} + {n2} = Par filhao')
            status = False
print(f'Voce ganhou {cont} vezes')