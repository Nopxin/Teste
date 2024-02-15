nome = '[ AUMENTO SALÁRIAL! ]'
print(f'{nome:=^60}\n')

s = float(input(' O salário do funcionário é R$'))
print(f' Todavia, a empresa concede 15% de aumento\n Que confere a R${s*0.15:.2f}\n O novo salário do funcionário com este aumento é dê R${s*0.15+s:.2f}')