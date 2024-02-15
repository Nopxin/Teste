nome = '[ PINTANDO UMA PAREDE ]'
print(f'{nome:=^60}\n')

l = float(input(' Qual é a largura de sua parede (em metros)? '))
h = float(input(' Qual é a altura de sua parede (em metros)? '))

print(f'\n Cada litro de tinta pode pintar até 2m² de parede\n Tendo em vista que a área de sua parede é de {l*h}m²\n É necessário {l*h/2}L de tinta para pintar toda a parede')