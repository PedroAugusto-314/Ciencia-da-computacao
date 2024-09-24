"""
13)Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. 
Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para 
indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir
"""
from funcoes import float_input
consumo = float_input("Qual seu consumo de energia elétrica em kwh? ")
instalacao = input("Qual seu tipo de instalação? R = residência, I = indústria e C = comércio: ").upper()
match instalacao:
    case 'R':
        print("Residência")
        if consumo <= 500: print(f"Preço a pagar: R${consumo*0.4:.2f}".replace('.',','))
        else: print(f"Preço a pagar: R${consumo*0.65:.2f}".replace('.',','))
    case 'C':
        print("Comércio")
        if consumo <= 1000: print(f"Preço a pagar: R${consumo*0.55:.2f}".replace('.',','))
        else: print(f"Preço a pagar: R${consumo*0.60:.2f}".replace('.',','))
    case 'I':
        print("Indústria")
        if consumo <= 5000: print(f"Preço a pagar: R${consumo*0.55:.2f}".replace('.',','))
        else: print(f"Preço a pagar: R${consumo*0.60:.2f}".replace('.',','))