"""
ler o salário base de um funcionário, dar 5% de gratificação e
descontar 7% de imposto
"""

salario = float(input(f'qual o salário base do funcionário?\n'))
print(f'o valor líquido do salário é R${salario + salario * 0.05 - salario * 0.07}')
