city = input(' Digite o nome de uma cidade: ')

ppn = city.find(' ')
city = city.upper()
pn = city.strip()

if 'SANTO' in pn:
    print(f' {city.title().strip()} começa com Santo.')

else:
    print(f' {city.title().strip()} não começa com Santo.')