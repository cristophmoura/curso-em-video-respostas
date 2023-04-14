n1 = (int(input('Digite um numero: ')),
      int(input('Digite outro numero: ')),
      int(input('Digite mais numero: ')),
      int(input('Digite o ultimo numero: ')))
n2 = []
pos3 = True
print(f'Voce digitou os valores {n1}')
print(f'O valor 9 aparece' , n1.count(9) , 'vezes')
for tabela in range(0,len(n1)):
      if n1[tabela] % 2 == 0:
            n2.append(n1[tabela])
      if n1.count(3) > 0:
            print(f'O primeiro valor 3 foi digitado na posição', n1.index(3))
      else:
            pos3 = False
if pos3 == False:
      print('Não foi digitado nenhum numero 3.')
print(f'Os números pares foram: ',n2)