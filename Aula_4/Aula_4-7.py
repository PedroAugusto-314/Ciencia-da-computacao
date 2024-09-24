"""
7) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado 
pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o 
preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""
from funcoes import float_input
km = float_input("Quantos km você percorreu com o carro? ")
dias = float_input("quantos dias você passou com o carro? ")
print(f'Você pagará R${dias*60+km*0.15:.2f} pelo aluguel do carro'.replace('.', ',') + '.')
