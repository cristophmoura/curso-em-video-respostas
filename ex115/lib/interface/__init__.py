def leiaInt(msg):
    while True:
        try:
            n = input(msg)
            n = int(n)
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um valor válido.\033[m')
            continue
        except (KeyboardInterrupt):

            print('\n\033[31mUsuário preferiu não digitar este número\033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[34m{c}\33[m - \033[37m{item}\33[m')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc