n = input(' Digite seu nome completo: ')

print(n.upper())
print(n.lower())

c = len(n)
s = n.count(' ')

print(f' Seu nome possúi {c-s} letras')

n1 = n.find(' ')

pn = n[:n1]
print(f' Seu primeiro nome, {pn}, possúi {len(pn)} letras.')
