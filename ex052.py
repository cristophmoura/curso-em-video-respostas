numero = int(input("Digite um número: "))

# Verifica se o número é primo
if numero > 1:
    for i in range(2, numero):
        if (numero % i) == 0:
            print(numero, "não é primo.")
            break
    else:
        print(numero, "é primo.")
else:
    print(numero, "não é primo.")
