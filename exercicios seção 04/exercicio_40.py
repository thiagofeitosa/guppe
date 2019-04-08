"""
ler quantas diarias de um encanador que recebe 30 reais por dia
e imprimir seu valor liquido com o desconto de 8% da empresa
"""

dias = int(input('quantos dias foram trabalhados?\n'))
print(f'o valor liquido a ser recebido é {dias * 30 - dias * 30 * 0.08}')
