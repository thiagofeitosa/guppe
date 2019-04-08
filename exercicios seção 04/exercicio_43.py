"""
ler um valor
imprimir desconto de 10%
valor dividido em 3x
comissão de 5% sobre o valor com desconto
comissão de 5% sobre o valor total
"""

valor = float(input('digite o valor da compra\n'))
print(f'valor com desconto é {valor - valor * 0.1}\n')
print(f'valor da parcela 3x {valor / 3}\n')
descontado = valor - valor * 0.1
print(f'valor da comissão com desconto {descontado - descontado * 0.95}\n')
print(f'valor da comissão compra dividida {valor - valor * 0.95}\n')
