'''
Exercício 05: Calcule o fatorial dos seguintes valores:

a) 5
b) 9
c) 12
d) 22
e) 9
'''
from math import factorial

def calcular_fatorial(alternativas):
    for altenativa in alternativas:
        print(altenativa)
        numero = int(altenativa.replace(' ', '').replace(',','.')[2:])
        print(f'Fatorial: {factorial(numero)}')
        print('-'*30)

calcular_fatorial(['a) 5', 'b) 9', 'c) 12', 'd) 22', 'e) 9'])
