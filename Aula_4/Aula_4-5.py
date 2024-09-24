"""
5) Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba 
o valor do desconto e o preço a pagar
"""
from funcoes import float_input

mercadoria = float_input("Digite o valor da mercadoria: ")
desconto = float_input("Digite a porcentagem de de desconto: ")
print(f'Valor do desconto: R${mercadoria*(desconto/100)}\nPreço final da mercadoria: R${mercadoria-(mercadoria*(desconto/100))}')
