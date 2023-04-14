ex058

import random
n1 = random.randint(0,11)
cont = 0
tentativa = 20
while n1 != tentativa:
    tentativa = int(input('Adivinha: '))
print(f"Acertou, o numero era {n1} e vc falou {tentativa}")