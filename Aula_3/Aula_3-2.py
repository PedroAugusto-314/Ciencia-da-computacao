"""
b) Sabendo que a quantidade de alunos na turma de PYTHON é igual a 32, faça uma estrutura condicional 
onde verifique se o número é maior que 30; neste caso, estes ganharão uma passagem para Cancun. Se 
for igual a 30, estes ganharão uma passagem para Fortaleza. Se for menor que 30, estes ganharão uma 
passagem para Caldas Novas. 
"""

TURMA_PYTHON : int = 32
if TURMA_PYTHON > 30: print('Ganharam uma passagem para Cancun')
elif TURMA_PYTHON == 30: print('Ganharam uma passagem para Fortaleza')
else: print('Ganharam uma passagem para Caldas Novas')