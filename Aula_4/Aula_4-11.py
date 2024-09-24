"""
11)Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. 
Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e 
R$ 0,45 para viagens mais longas.
"""
from funcoes import float_input
distancia = float_input("Qual distância em km você deseja percorrer? ")
if distancia > 200: print(f'O preço da passagem será: R${distancia*0.45:.2f}'.replace('.',','))
else: print(f'O preço da passagem será: R${distancia*0.50:.2f}'.replace('.',','))