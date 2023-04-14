choice = 0
resultado = 0
while choice != 6:
    n1 = int(input('Primeiro número: '))
    n2 = int(input('Segundo número: '))
    choice = int(input('Calculadora: 1.soma-2.multiplica-3.maior-4.novos numeros-5.sair'))
    if choice == 1:
        resultado = n1+n2
        print(f"A soma ficou: {resultado}\n")
    elif choice == 2:
        resultado = n1*n2
        print(f"A multiplicacao ficou {resultado}\n")
    elif choice == 3:
        if n1 > n2:
            print(f"O {n1} é maior")
        elif n1 < n2:
            print(f"O {n2} é maior")
        else:
            print('Os números são iguais')
    elif choice == 4:
        print('Digite os novos números')
    elif choice == 5:
       sair = input('Tem ctz que quer sair [S/N]? ').strip().upper()[0]
       if sair == 'S':
        choice = 6
print('FIM')