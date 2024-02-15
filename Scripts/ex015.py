nome = '[ ALUGUEL DE CARROS ]'
print(f'{nome:=^60}\n')

dias = int(input(' Quantos dias alugados? ')) *60
km = int(input(' Quantos Km rodados? ')) *0.15

print(f' O total a pagar é de R${(km+dias):.2f}')