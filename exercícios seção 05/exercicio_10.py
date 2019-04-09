"""
ler a altura e o gênero da pessoa e informar o peso ideal
homens = (72.7  *  h) - 58
homens = (62.1  *  h) - 44.7
"""

h = float(input('digite a sua altura\n'))
genero = input('digite o seu gênero M ou F')

if genero != 'M' or genero != 'F':
    print('gênero inválido.\n')
elif genero == 'M':
    print(f'seu peso ideal é {(72.7  *  h) - 58}\n')
else:
    print(f'seu peso ideal é {(62.1  *  h) - 44.7}\n')
