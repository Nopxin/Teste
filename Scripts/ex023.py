n = input(' Digite um número de 0 á 9999: ')
quant = len(n)


print(f' Dividindo o número {n}, conseguimos:')
if quant >= 1:
    print(f' Unidade: {n[3]}')

else:
    print(f' Unidade: 0')

if quant >= 2:
    print(f' Dezena: {n[2]}')

else:
    print(f' Dezena: 0')

if quant >= 3:
    print(f' Centena: {n[1]}')

else:
    print(f' Centena: 0')

if quant >= 4:
    print(f' Milhar: {n[0]}')

else:
    print(f' Milhar: 0')