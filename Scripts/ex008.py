nome = '[ CONVERSOR DE METROS PARA... ]'
print(f'{nome:=^60}')

m = float(input('\n Me diga um número em metros! '))
print(f' {m} metro(s) é igual a...\n\n {m/1000} quilômetros\n {m/100} hectômetros\n {m/10} decâmetros\n {m} metros\n {m*10} decímetros\n {m*100} centímetros\n {m*1000} milímetros')
