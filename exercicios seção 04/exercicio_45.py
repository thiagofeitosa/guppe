"""
converter maiuscula em minuscula usando tabela ascii Unicode
"""

maiuscula = ord(input('digite a letra maiúscula\n'))
print(f'a letra minuscula é {str(chr(maiuscula+32))}')
