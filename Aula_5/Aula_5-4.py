"""
4) Faça um algoritmo que, usando o comando “for”, calcule a soma dos números pares compreendidos no 
intervalo de 160 a 190. 
"""
soma : int = 0
for i in range(160,191,2): soma += i
print(f'A soma dos números é: {soma}')