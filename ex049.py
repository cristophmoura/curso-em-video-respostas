n1 = int(input('Digite um numero p ver a tabuada: '))
#x1 = int(n1*1)
cont = 0
tab = 0
for c in range(1,11):
    cont = cont + 1
    tab = n1 * cont
    print(f"{n1} x {cont} = {tab}")
