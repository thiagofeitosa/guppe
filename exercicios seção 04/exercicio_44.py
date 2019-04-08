"""
receba a altura de um degrau de uma escada e quanto de altura o usuário
deseja alcançar e mostre quantos degraus ele deve subir.
"""

degrau = float(input('qual a altura do degrau?\n'))
altura = float(input('qual a altura deseja alcançar?\n'))
print(f'você deve subir {int(altura / degrau)} degraus\n')
