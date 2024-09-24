"""
Exercício 03: Faça a verificação, conforme exemplo anterior, do resultado das operações das 
variáveis descritas. Escrever os resultados no caderno.
a) a = 7, b = 5
b) a = 20, b = 10
c) a = 8, b = 3
d) a = 1024, b = 512
e) a = 99, b = 53
"""

def calcular(a : int, b : int) -> None :
    print(f'''Soma: {a+b}\nSubtração: {a-b}\nMultiplicação: {a*b}\nDivisão: {a/b}\nDivisão inteira: {a//b}\nResto ou Modulo: {a%b}''')
    exp = a**b    
    print(f'Exponenciação: {exp if len(str(exp)) < 10 else exp:e}\n{'-'*30}')

calcular(7,5)
calcular(20,10)
calcular(8,3)
calcular(1024,512)
calcular(99,53)
