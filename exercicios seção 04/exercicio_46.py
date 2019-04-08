"""
ler um número inteiro e imprimir o número ao contrário
exemplo: 123 -> 321
"""

numero = str(input('digite o número a ser convertido\n'))
print(f'o número ao contrário é {int(numero[::-1])}')
