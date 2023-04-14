ano = 0
cont = 0
maior = 0
menor = 0
atual = 2023
for c in range(1,8):
    ano = int(input('Qual idade: '))
    if atual - ano > 18:
        maior += 1
    else:
        menor += 1
    cont += 1
print(maior, menor)