"""
ler um número, se for positivo, mostrar a raiz quadrada, se for negativo
mostrar ele ao quadrado
"""

numero = float(input('digite um número\n'))
if numero > 0:
    print(f'a raiz quadrada de {numero} é {numero ** 0.5}')
else:
    print(f'o número {numero} ao quadrado é {numero ** 2}')
