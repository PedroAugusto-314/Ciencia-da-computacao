'''
Exercício 04: Calcule o arredondamento par cima, para baixo e o valor absoluto para os seguintes valores:
a) 5,8
b) -9,7
c) -10,2
d) 33,6
e) -25,5
'''

from math import ceil, floor, fabs

def calcular(alternativas : str) -> None:
    for altenativa in alternativas:
        print(altenativa)
        numero = float(altenativa.replace(' ', '').replace(',','.')[2:])
        print(f'Arredondamento para cima: {ceil(numero)}\nArredondamento para baixo: {floor(numero)}\nValor absoluto: {fabs(numero)}')
        print('-'*30)

calcular(['a) 5,8' , 'b) -9,7', 'c) -10,2', 'd) 33,6' ,'e) -25,5'])
