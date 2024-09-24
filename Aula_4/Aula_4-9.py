"""
9) Escreva um programa que leia três números e que imprima o maior e o menor.
"""
from funcoes import float_input
x = float_input("Escreva um número: ")
y = float_input("Escreva mais um número: ")
z = float_input("Escreva um último número: ")
numeros = [x,y,z]
numeros.sort()
print(f"O maior número é: {numeros[-1]}, e o menor é {numeros[0]}")