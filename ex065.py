continuar = 'S'
n1 = cont = media = maior = menor = 0
while continuar == 'S':
    n1 = int(input('Digite um número: '))
    cont += 1
    media = (media+n1)/cont
    if cont == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
print(f"Vc digitou {cont} números e a média foi {media}")
print(f"O maior valor foi {maior} e o menor foi {menor}")
