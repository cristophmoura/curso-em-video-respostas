exp = str(input('Digite uma expressão'))
car = []

for p in range(len(exp)):
    if '(' in exp[p]:
        car.append('(')
    elif ')' in exp[p]:
        if '(' in car:
            car.remove('(')
        else:
            car.append(')')
if len(car) == 0:
    print('Ta certin')
else:
    print('Expressão está errada')
print(car)



""""
Essa lista retorna como correto uma expressão inválida como por ex:  )2+2(

lista = []
lista.append(str(input('Digita uma expressão aí malandro: ')))
contAberto = contFechado = 0
for p in lista:
    for letra in p:
        if letra in '({[':
            contAberto += 1
        elif letra in ')}]':
            contFechado += 1
if contAberto != contFechado:
    print('Algo de errado não está certo')
else:
    print('A expressão tá certin')"""