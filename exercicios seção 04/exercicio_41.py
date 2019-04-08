"""
ler valor de hora de trabalho em reais e número de horas trabalhadas em
um mês e imprimir o valor com acrescimo de 10%
"""

valor = float(input('digite o valor da hora do funcionário\n'))
horas = float(input('digite o número de horas trabalhadas no mês\n'))
print(f'o valor a ser recebido é R${valor * horas + valor * horas * 0.1}')
