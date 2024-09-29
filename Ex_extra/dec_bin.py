DICT_HEX = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}


def convert_bin_dec(num_bin: str) -> int:
    """
    conversão de número binário para decimal inteiro
    """
    for bit in num_bin:
        if bit not in '01':
            return 'Número inválido'

    num_dec : int = 0 
    for i, bit in enumerate(reversed(num_bin)):
        num_mult : int = int(bit)*2**i 
        num_dec+=num_mult 
    
    return num_dec


def convert_dec_bin(num_dec : int | float) -> str:
    """
    conversão de número decimal para binário inteiro
    """
    restos : list = []
    while num_dec != 1:
        restos.append(int(num_dec%2))
        num_dec //= 2
    
    restos.append(num_dec)
    restos.reverse()

    num_bin : str = ''
    for r in restos:
        num_bin += str(r)
    
    return num_bin



def convert_to_dec(num: str, base : int) -> int:
    """
    conversão de número de qualquer base para decimal
    num = um número em qualquer base
    base = 2 | 8 | 16, a base do número fornecido
    """

    match base:
        case 2:
            for n in num:
                if n not in '01': return 'Inválido'
        case 8:
            for n in num:
                if n not in '01234567': return 'Inválido'
        case 16:
            for n in num:
                if n not in '0123456789aAbBcCdDeEfF': return 'Inválido'

    num_dec : int = 0 
    for i, bit in enumerate(reversed(num)):
        if bit in 'aAbBcCdDeEfF':
            # match bit.upper():
            #     case 'A':bit = 10
            #     case 'B':bit = 11
            #     case 'C':bit = 12
            #     case 'D':bit = 13
            #     case 'E':bit = 14
            #     case 'F':bit = 15

            bit = DICT_HEX.get(bit.upper())
            
        num_mult : int = int(bit)*base**i 
        num_dec+=num_mult 
    
    return num_dec

print(convert_to_dec('f1',16))


def convert_dec(num_dec : int | float, base : int) -> str:
    """
    conversão de número decimal para qualquer outra base,
    num_dec = um número decimal qualquer
    base = 2 | 8 | 16, base para qual será convertida
    """

    restos : list = []
    while num_dec > base-1:
        resto = int(num_dec%base)
        # match resto:
        #     case 10: resto = 'A'           #opção 1
        #     case 11: resto = 'B'
        #     case 12: resto = 'C'
        #     case 13: resto = 'D'
        #     case 14: resto = 'E'
        #     case 15: resto = 'F'
        
        if resto in DICT_HEX.keys():        #opção 2
            resto = DICT_HEX.get(resto)


        restos.append(resto)
        num_dec //= base
    
    match num_dec:
        case 10: num_dec = 'A'
        case 11: num_dec = 'B'
        case 12: num_dec = 'C'
        case 13: num_dec = 'D'
        case 14: num_dec = 'E'
        case 15: num_dec = 'F'
    restos.append(num_dec)
    restos.reverse()

    num_bin : str = ''
    for r in restos:
        num_bin += str(r)
    
    return num_bin

print(convert_dec(241,16))