"""
ler dois números e imprimir o maior
"""

numero1 = int(input('digite o primeiro número\n'))
numero2 = int(input('digite o segundo número\n'))
if numero1 > numero2:
    print(f'O maior número é {numero1}\n')
elif numero2 > numero1:
    print(f'O maior número é {numero2}\n')
else:
    print('Os dois números são iguais\n')
