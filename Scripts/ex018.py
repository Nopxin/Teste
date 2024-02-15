import math

nome = '[ CÁLCULO DE SENO, COSSENO E TANGENTE ]'
print(f'{nome:=^60}\n')

a = int(input(' Digite o valor de um ângulo: '))

print(f'\n Falando sobre um ângulo dê {a}°, o valor de seu seno, cosseno e tangente é de...\n Cosseno: {math.cos(math.radians(a)):.3f}\n Seno: {math.sin(math.radians(a)):.3f}\n Tangente: {math.tan(math.radians(a)):.3f} ')
