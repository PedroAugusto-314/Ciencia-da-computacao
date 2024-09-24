'''
Exercício 07: Calcule a raiz quadrada dos seguintes números.
a) 39
b) 100
c) 45
d) 18
e) 6
'''
from math import sqrt

def calcular_raiz(alternativas):
    for altenativa in alternativas:
        print(altenativa)
        numero = int(altenativa.replace(' ', '').replace(',','.')[2:])
        print(f'Raiz Quadrada: {round(sqrt(numero), 2)}')
        print('-'*30)

calcular_raiz(['a) 39', 'b) 100', 'c) 45', 'd) 18', 'e) 6'])

print()



alternativa = 'a)39'
alternativa.replace()