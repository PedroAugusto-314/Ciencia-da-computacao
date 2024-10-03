import functions as f

DICT_HEX = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 
    10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'
}

DICT_TABELA_DE_CONVERSÕES_OCT_BIN = {
    '0': '000', '1': '001', '2': '010', '3': '011',
    '4': '100', '5': '101', '6': '110', '7': '111'
}

DICT_TABELA_DE_CONVERSÕES_HEX_BIN = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', 
    '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010',  'B': '1011', 
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}


def convert_to_dec(num: str, base : int) -> int:
    """
    conversão de número de qualquer base para decimal,
    num = um número em qualquer base;
    base = 2 | 8 | 16, a base do número fornecido
    """
    #Verificação
    verif_num = f.verificar_numero(num, base)
    if verif_num: return verif_num

    #Conversão
    num_dec : int = 0 
    for i, bit in enumerate(reversed(num)):
        if bit in 'aAbBcCdDeEfF': bit = DICT_HEX.get(bit.upper()) #Converter letra para número hex
        
        num_mult : int = int(bit)*base**i 
        num_dec+=num_mult 

    

    return num_dec



def convert_dec(num_dec : str | float, base : int) -> str:
    """
    conversão de número decimal para qualquer outra base,
    num_dec = um número decimal qualquer;
    base = 2 | 8 | 16, base para qual será convertida
    """
    #Verificação
    verif_num = f.verificar_numero(num_dec, 10)
    if verif_num: return verif_num

    num_dec = int(num_dec)

    #Conversão
    restos : list = []
    while num_dec > base-1:
        resto = int(num_dec%base)
        if resto in DICT_HEX.keys(): resto = DICT_HEX.get(resto) #Converter número resto para letra hex
        restos.append(str(resto))
        num_dec //= base
    
    if num_dec in DICT_HEX.keys(): num_dec = DICT_HEX.get(num_dec) #Converter número para letra hex
    
    restos.append(str(num_dec))
    restos.reverse()

    return f.list_to_str(restos)



def split_bits(numero_bin : str, qnt_bits : int)-> list:
    #preenchendo com 0 a esquerda
    tamanho = len(numero_bin)
    while tamanho%qnt_bits != 0:
        tamanho +=1
    numero_bin_preenchido = numero_bin.zfill(tamanho)

    #dividindo
    numero_bin_sep = []
    for i, x in enumerate(numero_bin_preenchido, 1):
        if i%qnt_bits == 0 and i > 0:
            numero_bin_sep.append(numero_bin_preenchido[i-qnt_bits:i])

    return numero_bin_sep

def convert_bin(numero: str, base: int) -> str:
    """
    Converte um número binário para Octal ou Hexadecimal,\n
    numero: O número binário a ser convertido,\n
    base = 8 | 16 :A base para qual será convertido
    """
    #Verificação
    verif_num = f.verificar_numero(numero, 2)
    if verif_num: return verif_num
    
    #Conversão
    num_bin_separado = split_bits(numero_bin=numero,qnt_bits=3 if base == 8 else 4)
    num_convertido = []
    tabela = DICT_TABELA_DE_CONVERSÕES_OCT_BIN if base == 8 else DICT_TABELA_DE_CONVERSÕES_HEX_BIN
    for num_bin in num_bin_separado:
        num_convertido.append(f.get_key(tabela, num_bin))

    return f.list_to_str(num_convertido)


def convert_to_bin(numero : str, base: int) ->str:
    """
    Converte um número octal ou hexadecimal para binário,\n
    numero : O número octal ou hexadecimal a ser convertido,\n
    base = 8 | 16: Indicação da base do número fornecido.
    """
    #Verificação do número digitado
    verif_num = f.verificar_numero(numero, base)
    if verif_num: return verif_num

    #Conversão
    numero = numero.upper()
    tabela = DICT_TABELA_DE_CONVERSÕES_HEX_BIN if base == 16 else DICT_TABELA_DE_CONVERSÕES_OCT_BIN
    num_sep = [tabela.get(n) for n in numero]
    return f.list_to_str(num_sep).lstrip('0')





def convert_hex_oct(numero : str, base_numero : int, base_converter : int):
    """
    Converte um número octal para hexadecimal e vice versa.\n
    numero : str = número a ser convertido,\n
    base_numero : int = 8|16 base do número fornecido,\n
    base_converter : int = 8|16 base para qual será convertido,\n
    """

    #Validação do número digitado 
    verif_num = f.verificar_numero(numero, base_numero)
    if verif_num: return verif_num

    #Conversão
    num_bin = convert_to_bin(numero=numero, base=base_numero)
    num_convertido = convert_bin(numero=num_bin, base=base_converter)
    return num_convertido





if __name__ == '__main__':
    pass
    # print(convert_to_dec('f',16))
    # print(convert_dec(241,16))




