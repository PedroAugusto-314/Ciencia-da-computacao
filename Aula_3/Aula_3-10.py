"""
6) Descreva o funcionamento da estrutura condicional.
"""
'''
A estrutura condicional, diferente da estrutura sequêncial, contém desvios de fluxo, onde algumas linhas podem ou não
ser executadas. Possui expressões lógicas que definem o fluxo do programa baseado no valor resultado dessas
expressões(verdadeiro ou falso).

Exemplo:
idade = 17
if idade >= 18:
    print("Você pode tirar a habilitação")
else:
    print("Você ainda não pode tirar a habilitação, aguarde até ter 18 anos")

Neste caso, a linha 'if idade >= 18:' verifica se o resultado da expressão é verdadeiro, se for, a linha
'print("Você pode tirar a habilitação")' será executada, ignorando o restante das linhas. Caso o resultado
não seja verdadeiro, a linha 'print("Você pode tirar a habilitação")' será ignorada, e o que está dentro do
'else'(senao), no caso, a linha 'print("Você ainda não pode tirar a habilitação, aguarde até ter 18 anos")',
será executada.
'''