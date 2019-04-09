"""
ler um número, se for positivo, mostrar a raiz quadrada, se for negativo
mostrar que é inválido
"""

numero = float(input('digite um número positivo\n'))
if numero > 0:
    print(f'a raiz quadrada de {numero} é {numero ** 0.5}')
else:
    print('número inválido, digite um número positivo')
