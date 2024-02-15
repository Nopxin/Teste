nome = '[ CÁLCULO DE MÉDIA ]'
print(f'{nome:=^60}\n')

n1 = float(input(' Me diga a primeira nota! '))
n2 = float(input(' Me diga a segunda nota! '))

print(f'\n A média do aluno com notas {n1} e {n2} é...\n Sem arredondamento: {(n1+n2)/2}\n Com arredondamento: {round((n1+n2)/2)}')