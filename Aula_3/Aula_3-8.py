"""
4) Faça um algoritmo que dado os valores A=7, B=9, C=3, D=4, calcule sua média. Converta para 
PYTHON.
"""
from funcoes import cprint, cinput, clear
# A, B, C, D = 7, 9, 3, 4
# print(f'A média entre A, B, C e D é {(A+B+C+D)/4}')

numeros = []
clear()
while True:
    print("Aperte 'enter' sem digitar nada para confirmar e calcular a média")
    numero = cinput("Digite um número para calcular a média: ")
    if numero:
        if numero.isnumeric(): 
            numeros.append(int(numero))
        else: 
            cprint('Digite um número válido!')
    else:
        if len(numeros) < 1: 
            print('Você não digitou nenhum número')
            break
        else: 
            print(f'A média entre {numeros} é: {sum(numeros)/len(numeros):.2f}')
            break
