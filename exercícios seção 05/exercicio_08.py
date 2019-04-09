"""
ler duas notas entre 0.0 e 10.0 e imprimir a média delas
"""

nota1 = float(input('digite a nota 1\n'))
if 0.0 > nota1 or nota1 > 10.0:
    print(f'o valor {nota1} é inválido\n')
else:
    nota2 = float(input('digite a nota 2\n'))
    if 0.0 > nota2 or nota2 > 10.0:
        print(f'o valor {nota2} é inválido\n')
    else:
        print(f'a média das notas é {(nota1 + nota2) / 2}')
