p = input(' O que você vai colher (escreva no singular)? ')
dp = int(input(f' Em que dia você vai começar o plantio de {p}? '))

dpo = dp

fe = int(input(f' Em que dia você finaliza o plantio/estação? '))
tc = int(input(f' Quantos dias demora para o crescimento de {p}? (caso não seja de colheita múltipla, digite 0): '))
cc = int(input(f' Quantos dias possui o ciclo de colheita de {p}? '))

ps = int(input(f' Quanto custa uma semente de {p}? '))
vc = int(input(f' Quanto custa uma colheita de {p}? '))

qp = int(input(f' Quantas sementes de {p} você irá plantar? '))

print(f'\n A colheita de {p} vai acontecer nos dias', end='')

c = 0

while dp < fe:
    if tc != 0 and c == 0:
        dp = dp + tc
        c = c + 1
        print(f' {dp}', end='')

    dp = dp + cc
    if dp > fe:
        dp = dp - cc
        break
    if dp + cc > fe:
        print(f' e {dp}', end='')
    elif dp == dpo + cc:
        print(f' {dp}', end='')
    else:
        print(f', {dp}', end='')

    c = c+1

print(' da estação em questão.')

prejuizo = c*ps
lucro = c*vc*qp

print(f' Seguindo as infromações acima, após {fe-dpo} dias e {c} colheitas de\n {p}, o valor arrecadado é de', end=' ')
if tc == 0:
    print(lucro-prejuizo, 'Ouros')

else:
    print(lucro-ps, 'Ouros')