"""
3) Como funciona a estrutura sequencial?
"""
'''
-A estrutura sequêncial é aquela onde o código é lido e executado de forma sequencial, uma instrução após a outra,
linha a linha, de cima pra baixo e da esquerda pra direita. 
Exemplo:
msg = "Hello World!"
print(msg)
-Neste caso, cada linha será executada na ordem em que foram escritas, não havendo nenhuma quebra ou
desvio de fluxo. Diferente do caso abaixo, que já foge da estrutura sequêncial
msg = "Hello World!"
if msg:
    print(msg)
else:
    print("Não há nenhuma mensagem")
-Neste caso, dependendo do conteúdo da variável 'msg', a forma como o código é executado muda, podendo
ignorar ou ler as linhas 'print(msg)' e 'print("Não há nenhuma mensagem")'
'''
