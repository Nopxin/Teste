nome = '[ CONVERSOR D/ REAL P/ DÓLAR ]'
print(f'{nome:=^60}\n')

din = float(input(' Quanto você possui em sua carteira? R$'))

print(f'\n Tendo R${din:.2f} (reais), é possível comprar ${din/4.92:.2f} (dólares)')