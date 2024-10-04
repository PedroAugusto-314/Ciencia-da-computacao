from utils import functions as f
from conversor import conversoes

SOMA_DICT = {
    ('0','0','0') : ('0','0'),
    ('0','0','1') : ('1','0'),
    ('1','0','0') : ('1','0'),
    ('1','0','1') : ('0','1'),
    ('0','1','0') : ('1','0'),
    ('0','1','1') : ('0','1'),
    ('1','1','0') : ('0','1'),
    ('1','1','1') : ('1','1'),
}
SUB_DICT = {
    ('0','0','0') : ('0','0'),
    ('0','0','1') : ('1','1'),
    ('1','0','0') : ('1','0'),
    ('1','0','1') : ('0','0'),
    ('0','1','0') : ('1','1'),
    ('0','1','1') : ('0','1'),
    ('1','1','0') : ('0','0'),
    ('1','1','1') : ('1','1'),
}


def soma_sub_bin(num_1: str, num_2: str, operacao:str) -> str:
    
    #Definições de variáveis
    tabela = SOMA_DICT if operacao == '+' else SUB_DICT
    negativo = True if conversoes.convert_to_dec(num_1,2)<conversoes.convert_to_dec(num_2,2) and operacao == '-' else False

    num_1,num_2 = f.preencher(num_1,num_2)
    r = '0'
    numeros_soma = (num_1[::-1], num_2[::-1])
    resultado_soma = []

    #Calculo com base na tabela
    for i in range(len(num_1)):
        x = numeros_soma[0][i]
        y = numeros_soma[1][i]
        result = tabela.get((x,r,y))
        resultado_soma.append(result[0])
        r = result[1]
    if r == '1': resultado_soma.append(r)

    resultado_soma.reverse()

    #Complemento de 2 se o número for negativo
    if negativo: return f"{1}  {soma_sub_bin(f.list_to_str(['0' if n =='1' else '1' for n in resultado_soma]), '1', '+')}"

    return f.list_to_str(resultado_soma)


def multi(num_1: str, num_2: str) ->str:
    resultado = [num_1 if num == '1' else '0' for num in reversed(num_2)]
    
    for i in range(len(resultado)):
        resultado[i] = resultado[i].ljust(len(resultado[i])+i,'0')

    
    resultado_deslocado = f.preencher_valores_da_lista(resultado)
    soma = resultado_deslocado[0]
    for i in range(1,len(resultado_deslocado)):
        soma = (soma_sub_bin(soma, resultado_deslocado[i], '+'))
    
    return soma
        