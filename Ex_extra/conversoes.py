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

def convert_to_dec(num: str, base : int) -> int:
    """
    conversão de número de qualquer base para decimal,
    num = um número em qualquer base;
    base = 2 | 8 | 16, a base do número fornecido
    """
    #Verificar se digitou um número válido
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

    #Conversão
    num_dec : int = 0 
    for i, bit in enumerate(reversed(num)):
        if bit in 'aAbBcCdDeEfF': bit = DICT_HEX.get(bit.upper()) #Converter letra para número hex
            
        num_mult : int = int(bit)*base**i 
        num_dec+=num_mult 

    return num_dec


def convert_dec(num_dec : int | float, base : int) -> str:
    """
    conversão de número decimal para qualquer outra base,
    num_dec = um número decimal qualquer;
    base = 2 | 8 | 16, base para qual será convertida
    """

    restos : list = []
    while num_dec > base-1:
        resto = int(num_dec%base)
        
        if resto in DICT_HEX.keys(): resto = DICT_HEX.get(resto) #Converter número resto para letra hex

        restos.append(resto)
        num_dec //= base
    
    if num_dec in DICT_HEX.keys(): num_dec = DICT_HEX.get(num_dec) #Converter número para letra hex
    
    restos.append(num_dec)
    restos.reverse()

    #Converte resultado final para uma str
    num_bin : str = '' 
    for r in restos:
        num_bin += str(r)
    
    return num_bin

if __name__ == '__main__':
    print(convert_to_dec('f1',16))
    print(convert_dec(241,16))