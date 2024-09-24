"""
c) Verifique qual foi o valor de sua compra numa determinada loja (sugestão: R$ 637,78). Se o valor total 
for maior que R$ 150,00, pegar este valor, calcular o desconto de 10% e escrever na tela o novo valor 
total. Se for igual a R$ 150,00, calcular o desconto de 7% e escrever na tela o novo valor total. Se for 
menor que R$ 150,00, calcular o desconto de 4% e escrever na tela o novo valor total.
"""

compra : float = float(input("Qual foi o valor da sua compra? "))

if compra > 150: print(f"Valor com 10% de desconto: {compra*0.9:.2f}")
elif compra == 150: print(f"Valor com 7% de deconto: {compra*0.93:.2f}")
else: print(f"Valor com 4% de deconto: {compra*0.96:.2f}")











