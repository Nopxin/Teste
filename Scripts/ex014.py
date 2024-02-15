nome = '[ CONVERSOR DE TEMPERATURA ]'
print(f'{nome:=^60}\n')

t = float(input(' Digite uma temperatura em graus Celsius: '))

print(f' {t} °C equivale a...\n\n {t*9/5+32} °F\n {t+273.15} K')
