import random
n1 = random.randint(0,5)
tentativa = int(input('Tenta adivinhar o numero de 0 a 5: '))

print('Acertou' if tentativa == n1 else 'Errou')
print(n1)