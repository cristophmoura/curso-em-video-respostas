numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n1 = int(input('Digite um número: '))
continua = True
while continua == True:
    if 0 <= n1 <= 20:
        print(f'{numeros[n1]}')
        continua == False
        break
    else:
        n1 = int(input('Tem que ser entre 0 e 20: '))

