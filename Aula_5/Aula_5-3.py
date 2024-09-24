"""
3) Faça um algoritmo que calcule qual o valor final da aplicação, durante um período que será digitado por
você, sabendo que a taxa da aplicação é de 10% ao mês. Exemplo:
Valor = R$ 1000,00
Quantidade de meses = 3
1 ̊ mês: 1000 * 1.1 = 1100,00
2 ̊ mês: 1100 * 1.1 = 1210,00
3 ̊ mês: 1210 * 1.1 = 1331,00
# """
from funcoes import float_input, int_input

valor : float = float_input("Qual o valor da aplicação? ")
mes : int = int_input("Quantos meses ficará aplicado? ")
for i in range(1, mes+1): 
    valor *= 1.1
    print(f'{i}° mês = {valor:.2f}')

