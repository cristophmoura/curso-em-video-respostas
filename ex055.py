peso = []
cont = 0
for c in range(0,6):
    peso.insert(cont, int(input('Peso: ')))
    cont += 1
rev = sorted(peso, reverse=True)
print(rev)