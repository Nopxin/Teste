nome = '[ 5% DE DESCONTO! ]'
print(f'{nome:=^60}\n')

p = float(input(' O preço do produto é de R$'))

print(f' Todavia, com 5% de desconto, seu novo preço é de:\n R${((p*0.05)-p)*-1:.2f}, com R${p*0.05:.2f} de desconto!')