frase = ' Eu quero sentar pra bandido '

print(frase[9])
# A contagem de micro espaços conta com o zero

print(frase[9:13])
# O fatiamento ignora o ultimo número

print(frase[9:21:2])
# Início, fim e pulo (de quantos em quantos caracteres, um é escolhido)

print(frase[:9])

print(frase[15:])

print(frase[9::3])


print(len(frase))

print(frase.count('o', 0, 13))
# Caractere para contagem, inicio da contagem e fim

print(frase.find('bandido'))

print('Curso' in frase)

print(frase)

print(frase.replace('pra bandido', 'pro chefe, da cintura ignorante'))

print(frase.upper())
print(frase.title())

print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())

frase2 = frase.split()

print(frase2)
print('-'.join(frase2))
