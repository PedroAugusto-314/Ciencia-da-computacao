"""
c) converta R$ 3.657,38 para dólar ($). Usar para o algoritmo a formula: $1,00 = R$ 5,75.
"""

vreal : float = 3657.38
vdolar : str = f'{vreal/5.75:.2f}'
print(f'R$ 3.657,38 em dólar é: U$ {str(vdolar).replace('.',',')}')

input('Escreva seu nome')