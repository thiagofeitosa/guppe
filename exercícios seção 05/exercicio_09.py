"""
ler o salário de uma pessoa e o valor de um empréstimo
se o emprestimo for maior que 20% do salário não conceder
"""

salario = float(input('digite o valor do salário\n'))
emprestimo = float(input('digite o valor da prestação\n'))

if emprestimo > salario * 0.2:
    print('empréstimo não concedido\n')
else:
    print('empréstimo concedido\n')
