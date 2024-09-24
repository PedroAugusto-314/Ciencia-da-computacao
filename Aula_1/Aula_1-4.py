"""
d) Converter as variáveis vreal = 2657.38, vdolar = 5.67 de dollar
"""

vreal : float = 2657.38
vdolar : str = f'{vreal/5.67:.2f}' 
print(f'Com o dólar na cotação de U$ 5,67, R$ 2.657,38 convertido em dólar é: U$ {str(vdolar).replace('.',',')}')