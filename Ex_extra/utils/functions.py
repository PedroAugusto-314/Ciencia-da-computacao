def get_key(dict: dict, value:str|int) -> str | int:
    """Return the key for given value of a dictionary"""
    for k,v in dict.items():
        if value == v:
            return k
    return "Valor não existe"

def list_to_str(list:list) -> str :
    result = ''
    for n in list: result += n
    return result

def verificar_numero(numero: str, base : int) -> str | None:
    for n in numero:
        if base == 8 and n not in '012345678': return "Número Octal inválido" 
        if base == 16 and n not in '0123456789aAbBcCdDeEfF': return "Número Hexadecimal inválido"
        if base == 2 and n not in '01': return 'Número Binário inválido'
        if base == 10 and n not in '0123456789': return "Número Decimal inválido"
    return None

def preencher(num_1: str, num_2: str) -> str:
    if len(num_1) > len(num_2): num_2 = num_2.zfill(len(num_1))
    else: num_1 = num_1.zfill(len(num_2))

    return num_1,num_2


def preencher_valores_da_lista(lista_strings: list) -> None:
    lista_ordenada = lista_strings.copy()
    lista_ordenada.sort()
    maior = len(lista_ordenada[-1])
    lista_preenchida = [elemento.zfill(maior) for elemento in lista_strings]
    return lista_preenchida