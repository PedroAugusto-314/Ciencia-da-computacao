"""
Exercício 02: Agora, faça um programa em Python que escreva sua matrícula, o curso que você estuda e quantos 
anos você tem. Faça as mesmas referências do exercício anterior: 
(verifique a referência de memória de cada variável em Hexadecimal e os tipos de variáveis usadas).
"""

matricula : str = 'Pedro Augusto'
curso : float = 85.1
idade : int = 19
print(f'Meu curso: {curso}\nMinha matrícula: {matricula}\n{'-' * 40}')
print(f"Id da variável 'matricula': {hex(id(matricula))}\nTipo da variável 'matricula': {type(matricula)}\n{'-' * 40}")
print(f"Id da variável 'curso': {hex(id(curso))}\nTipo da variável 'curso': {type(curso)}\n{'-' * 40}")
print(f"Id da variável 'idade': {hex(id(idade))}\nTipo da variável 'idade': {type(idade)}")
