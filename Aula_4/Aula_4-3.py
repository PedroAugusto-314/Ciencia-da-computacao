"""
3) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
Calcule o total em segundos.
"""
from funcoes import float_input
dias = float_input("Escreva uma qunatidade em dias: ")
horas = float_input("Escreva uma qunatidade em horas: ")
minutos = float_input("Escreva uma qunatidade em minutos: ")
segundos = float_input("Escreva uma quantidade me segundos: ")

print(f"A quantidade total do do que você digitou, em segundos, é: {(dias*24*60*60)+(horas*60*60)+(minutos*60)+segundos} segundos") 