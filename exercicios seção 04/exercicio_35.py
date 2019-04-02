"""
ler o tamanho dos catetos e imprimir a hipotenusa
"""

cateto_a = float(input('digite o tamanho do cateto a\n'))
cateto_b = float(input('digite o tamanho do cateto b\n'))
print(f'a hipotenusa é {(cateto_a ** 2 + cateto_b ** 2) ** 0.5}')
