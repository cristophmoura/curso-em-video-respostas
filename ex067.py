n1 = int(input('Digite um numero p ver a tabuada: '))
cont = tab = 0
while n1 > 0:
    for c in range(1, 11):
        cont = cont + 1
        tab = n1 * cont
        print(f"{n1} x {cont} = {tab}")
    n1 = int(input('Digite um numero p ver a tabuada: '))
print('FIM')