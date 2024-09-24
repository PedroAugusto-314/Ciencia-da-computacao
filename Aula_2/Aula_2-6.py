'''
Exercício 06: Calcule o maior divisor comum dos seguintes pares:
a) (5,35)
b) (9, 12)
c) (1024, 512)
d) (22,44)
e) (36,90)
'''

from math import gcd
def calcular_mdc(alternativas):
    for altenativa in alternativas:
        print(altenativa)
        nums = altenativa[1:].replace(' ', '').replace(')','').split('(')[1].split(',')
        print(f'MDC: {gcd(int(nums[0]), int(nums[1]))}')
        print('-'*15)

calcular_mdc(['a) (5,35)', 'b) (9, 12)', 'c) (1024, 512)', 'd) (22,44)', 'e) (36,90)'])



# def fatoracao(x: int):
#     fatoracao_x = []
#     for i in range(2,10):
#         while x%i == 0:
#             fatoracao_x.append(i)
#             x = x/i

#     return fatoracao_x

# def verificar_repeticao(numero, lista_num):
#     repeticoes = 0
#     for num in lista_num:
#         if numero == num:
#             repeticoes += 1
#     return repeticoes

# def mdc(x, y):
#     fatoracao_x = fatoracao(x)
#     fatoracao_y = fatoracao(y)
#     for num in fatoracao_x:
#         if num in fatoracao_y:
#             verificar_repeticao(num, fatoracao_y)



    