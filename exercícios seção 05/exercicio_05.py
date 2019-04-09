"""
ler um número inteiro e verificar se é par ou ímpar
"""

numero = int(input('digite um número inteiro\n'))
if numero % 2 == 0:
    print(f'o número {numero} é par\n')
else:
    print(f'o número {numero} é ímpar\n')