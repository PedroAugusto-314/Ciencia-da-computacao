"""
Exercício 01: Agora, faça um programa em Python que escreva seu nome e seu peso, verifique a referência de memória 
de seu nome e idade em Hexadecimal. Agora, verifique, via código Python, os tipos de variáveis que você usou.
"""

nome : str = 'Pedro Augusto'
peso : float = 85.1
print(f'Meu nome: {nome}\nMeu peso: {peso}\n{'-' * 40}')
print(f"Id da variável 'nome': {hex(id(nome))}\nTipo da variável 'nome': {type(nome)}\n{'-' * 40}")
print(f"Id da variável 'peso': {hex(id(peso))}\nTipo da variável 'peso': {type(peso)}\n{'-' * 40}")
