"""
4) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário 
e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
"""
from funcoes import float_input

salario = float_input("Digite o valor do seu salário: ")
aumento = float_input("Digite a porcentagem de aumento que você deseja: ")
print(f'Seu salário: R%{salario}\nPorcentagem de aumento: {aumento}%\nSeu salário com aumento: R%{salario*(1+aumento/100):.2f}')