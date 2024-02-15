frase = input(' Digite uma frase: ')

frase = frase.strip().upper()

print(f' Sua frase possúi {frase.count('A')} letras "a".')
print(f' A primeira letra "a" aparece na posição {frase.find('A')}.')
print(f' A última letra "a" aparece na posição {frase.rfind('A')}.')