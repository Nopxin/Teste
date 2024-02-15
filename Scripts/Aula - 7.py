# Para criar linhas com nomes centralizados ou semelhantes, o código usado é:
# print(f'{*variável* : *caractere copiado* *setinha para direção* *quantidade de repetições*}')
# segue o exemplo abaixo:

nome = ' JOGO '
print(f'{nome:=^20}')

# lembrando, é importante sempre por o comando entre aspas (precedidas por um f), consequentemente, em chaves.

# Para limitar as casas decimais de um resultado, é necessário o comando a seguir:
# {num:.2f}
# seguindo do exemplo logo abaixo

num = 10/3
print(num)
print(f'{num:.2f}')

# tambem é possível a junção e quebra de linhas, sendo:
# junção: end=''
# quebra: /n
# seguimos com sua utilização:

print(' Olá, eu sou um inscrito', end=' ')
print(f'do guanabara! \n me auto apelidei de nop, mas isso fica para a próxima linha')
