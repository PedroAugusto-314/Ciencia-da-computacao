"""
12)Escreva um programa que leia dois números e que pergunte qual operação você deseja 
realizar. Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba 
o resultado da operação solicitada
"""
from funcoes import float_input, soma, subtracao, multiplicacao, divisao
x = float_input("Digite um número: ")
y = float_input("Digite mais um número: ")
operacao = input("Qual operação você deseja realizar? ")

operacoes = {
    '+' : soma,
    '-' : subtracao,
    '*' : multiplicacao,
    '/' : divisao
    }
print(f'{x}{operacao}{y} = {operacoes[operacao](x,y)}')

# match operacao:
#     case '+':
#         print(f'{x}+{y}={x+y}')
#     case '-':
#         print(f'{x}-{y}={x-y}')
#     case '*':
#         print(f'{x}*{y}={x*y}')
#     case '/':
#         print(f'{x}/{y}={x/y}')

# if operacao == '+': print(f'{x}+{y}={x+y}')
# elif operacao == '-': print(f'{x}-{y}={x-y}')
# elif operacao == '*': print(f'{x}*{y}={x*y}')
# elif operacao == '/': print(f'{x}/{y}={x/y}')
