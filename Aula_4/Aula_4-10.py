"""
10)Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou 
iguais, de 15%.
"""
from funcoes import float_input
salario = float_input("Qual o valor do seu salário? ")
if salario > 1250: print(f"Aumento de 10%: {salario*1.1:.2f}")
else: print(f"Aumento de 15%: {salario*1.15:.2f}")