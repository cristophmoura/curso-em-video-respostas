import math
graus = int(input('Digite os graus: '))
cos = math.cos(math.radians(graus))
sin = math.sin(math.radians(graus))
print('O cos de {} é {:.2f} e a sin é {:.2f}' .format(graus, cos, sin))