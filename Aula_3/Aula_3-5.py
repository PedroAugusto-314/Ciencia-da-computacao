"""
e) Verifique a quantidade de boas ações que você realizou hoje. Se for menor que 5, escreva que você é 
uma pessoa bacana; se for igual a 5, escreva que você é uma pessoa carismática; se for maior que 5, 
escreva “TU TÁ ANIMADO”
"""

acoes : int = int(input("Quantas boas ações você realizou hoje? "))

if acoes < 5: print("Você é uma pessoa bacana") 
elif acoes == 5: print("Você é uma pessoa carismática")
else: print("TU TÁ ANIMADO")
