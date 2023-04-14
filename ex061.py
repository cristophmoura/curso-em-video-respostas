""" --- Usando FOR ---

n1 =int(input("Primeiro elemento: ") )
razao = int(input("Razao: ") )
n = int(input("Quantos elementos exibir: ") )

ultimo = n1 + (n-1)*razao
ultimo = ultimo + 1

for var in range(n1, ultimo, razao):
    print(f"{var} > ", end="")"""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f"{termo} > ", end='')
    termo += razao
    cont += 1
print('FIM')
