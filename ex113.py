def leiaInt():
    while True:
        try:
            n = input('Digite um numero inteiro: ')
            n = int(n)
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um valor válido.\033[m')
            continue
        except (KeyboardInterrupt):

            print('\n\033[31mUsuário preferiu não digitar este número\033[m')
            return 0
        else:
            return n


def leiaFloat():
    while True:
        try:
            n = input('Digite um numero real: ')
            n = float(n)
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um valor válido.\033[m')
            continue
        except (KeyboardInterrupt):

            print('\n\033[31mUsuário preferiu não digitar este número\033[m')
            return 0
        else:
            return n


n1 = leiaInt()
n2 = leiaFloat()
print(f'O número inteiro digitado foi {n1} e o real foi {n2}')


