primeiro_termo = int(input("Digite o primeiro termo da progressão: "))
razao = int(input("Digite a razão da progressão: "))

for c in range(primeiro_termo, primeiro_termo + 10 * razao, razao):
    print(c)
