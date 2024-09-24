"""
7) Faça um algoritmo que escreva seu nome, endereço e número da sua casa. Se o número de sua casa 
for menor que 65, escrever na tela que: você pagará o IPTU deste ano parcelado em 3 vezes; se for igual 
a 65, você pagará o IPTU em duas parcelas; se for maior 65, você pagará o IPTU à vista. Converta para 
PYTHON.
"""
from funcoes import cprint, cinput, clear

clear()
nome : str = cinput("Qual o seu nome? ")
endereco : str = cinput("Qual o seu endereço? ")
while True:
    numero : str = cinput("Qual o número da sua casa? ")
    
    if numero.isnumeric():
        numero: int = int(numero)
        if numero < 65: cprint(f"{nome}, Você pagará o IPTU deste ano parcelado em 3 vezes") 
        elif numero == 65: cprint(f"{nome}, Você pagará o IPTU em duas parcelas")
        else: cprint(f"{nome}, Você pagará o IPTU à vista")
        break
    else: 
        cprint('Digite um número de casa Válido')
        
