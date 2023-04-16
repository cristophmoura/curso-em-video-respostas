altura = float(input('Qual a altura? '))
peso = float(input('Qual o peso? '))
imc = peso / (altura*altura)
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso Ideal')
elif 25 <= imc <= 30:
    print('Sobrepeso')
elif  30 <= imc <= 40:
    print('Obesidade')
else:
    print('Mórbida')
