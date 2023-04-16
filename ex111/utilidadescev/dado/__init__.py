from ex111.utilidadescev import moeda
def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: "{entrada}" é um preço inválido\033[m')
        else:
            valido = True
            return float(entrada)




    while True:
        if a == '':
            print(f'ERRO! "" é um preço inválido!')
            a = input('Digite o preço: R$')
        elif a.isnumeric():
            break
        else:
            print(f'ERRO! "{a}" é um preço inválido!')
            a = input('Digite o preço: R$')
