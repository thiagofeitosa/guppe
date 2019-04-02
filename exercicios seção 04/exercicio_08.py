"""
ler uma temperatura em kelvin e apresentar em celcius

C=(F-32)/1,8
"""

kelvin = float(input('digite a temperatura em kelvin\n'))
celcius = kelvin - 273.15
print(f'a temperatura em celcius é {celcius}')
