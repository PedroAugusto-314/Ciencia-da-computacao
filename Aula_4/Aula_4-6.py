"""
6) Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para 
a conversão é:
F = (9 * C) / 5 + 32
"""
from funcoes import float_input
temp_c = float_input("Digite um valor de temperatura em °C: ")
print(f"{temp_c}°C em °F é: {(temp_c*9)/5+32:.2f}")
