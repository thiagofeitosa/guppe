"""
ler uma temperatura em Celcius e apresentar em farenrait

C=(F-32)/1,8
"""

farenheit = float(input('digite a temperatura em farenheit\n'))
celcius = 5.0 * (farenheit - 32.0) / 9.0
print(f'a temperatura em farenheit é {celcius}')
