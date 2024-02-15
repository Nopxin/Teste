nome = '[ CÁLCULO DE HIPOTENUSA ]'
print(f'{nome:=^60}\n')

from math import sqrt

ca = float(input(' Digite o comprimento do cateto adjacente: '))
co = float(input(' Digite o comprimento do cateto oposto: '))

h = (ca ** 2 + co ** 2) ** 0.5

print(f'\n A soma do qusua adrado dos catetos é igual a hipotenusa\n Quê, de cateto adjacente {ca} e cateto oposto {co}\n Recebe um valor de {h:.2f}')