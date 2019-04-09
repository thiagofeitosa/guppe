"""
dado dois números mostrar o maior e a diferença entre eles
"""

num1 = int(input('digite o primeiro número\n'))
num2 = int(input('digite o segundo número\n'))
if num1 > num2:
    print(f'o maior número é {num1} e a diferença entre eles é {num1 - num2}\n')
else:
    print(f'o maior número é {num2} e a diferença entre eles é {num2 - num1}\n')