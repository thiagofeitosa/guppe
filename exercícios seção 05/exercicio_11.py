"""
ERRO


ler um número maior que zero e imprimir a soma dos seus algarísmos
"""

numero = input('digite um número inteiro maior que zero\n')
if numero < 0:
    print('número inválido\n')
else:
    str(numero)
    print(f'{type(numero)}')
    print(f'a soma é {numero[::1]}\n')
