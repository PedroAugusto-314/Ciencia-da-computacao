"""
d) verifique a quantidade de pontos na carteira no período de 1 (hum) ano. Se a quantidade de pontos for 
menor que 5, escreva que você, apesar da multa, é um bom(boa) condutor(a); se for igual a 5, escreva 
que, apesar de ser um bom condutor, tome cuidado; se for maior que 5, escreva que você é uma pessoa 
legal mas tem que prestar mais atenção às leis de trânsito.
"""
pontos : float = float(input("Qual a quantidade de pontos na sua carteira? "))

if pontos < 5: print("Apesar da multa, você é um bom condutor") 
elif pontos == 5: print("Apesar de ser um bom condutor, tome cuidado")
else: print("Você é uma pessoa legal mas tem que prestar mais atenção às leis de trânsito.")
