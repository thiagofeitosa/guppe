"""
ler um valor em real e a cotação do dólar e apresentar o valor em dólar
"""

real = float(input('digite um valor em real\n'))
cotacao = float(input('digite a cotação atual do dólar\n'))
print(f'o valor em dólar é {real / cotacao}')
