nome = input(' Digite seu nome completo: ')

nome = nome.upper().strip().split()

print(f''' 
O primeiro nome é: {nome[0].capitalize()}
O último nome é: {nome[len(nome)-1].capitalize()}
''')
