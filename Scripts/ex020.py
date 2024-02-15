import random

nome = '[ SORTEIO DE ORDEM ]'

print(f'{nome:=^60}\n')

n1 = input(' Qual o nome do primeiro aluno? ')
n2 = input(' Qual o nome do segundo aluno? ')
n3 = input(' Qual o nome do terceiro aluno? ')
n4 = input(' Qual o nome do quarto aluno? ')

nomes = [n1, n2, n3, n3]
print(f' Entre {n1}, {n2}, {n3} e {n4}, a ordem escolhidda é {nome}')

random.shuffle(nomes)
print(nomes)
