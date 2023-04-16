n1 = int(input('Digite um numero [999 para parar]: '))
soma = cont = 0

while n1 != 999:
        soma += n1
        cont += 1
        n1 = int(input('Digite um numero [999 para parar]: '))
print(f"A soma de {soma} números foi: {cont}")
