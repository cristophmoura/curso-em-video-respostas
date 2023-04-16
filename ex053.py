f = list(input('frase: '))
r = list(reversed(f))
resf = [c for c in f if c.strip()]
resr = [c for c in r if c.strip()]
if resf == resr:
    print('é igual')
else:
    print('nao é')
