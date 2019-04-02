"""
ler uma temperatura em Celcius e apresentar em farenrait

C=(F-32)/1,8
"""

celcius = float(input('digite a temperatura em celcius\n'))
farenheit = celcius * (9.0 / 5.0) + 32.0
print(f'a temperatura em farenheit é {farenheit}')
