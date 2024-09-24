from os import system
def clear():
    system('cls')

def cprint(*args):
    clear()
    print(*args)

def cinput(*args):
    inp = input(*args)
    clear()
    return inp

def int_input(texto : str) -> int:
    clear()
    while True:
        x = input(texto)
        if x.isnumeric():
            return int(x)
        else:
            clear()
            print("Você não digitou um número inteiro válido")

def float_input(texto : str) -> int:
    clear()
    while True:
        x = input(texto)    
        try:
            x = float(x)
            return x
        except ValueError:
            clear()
            print("Você não digitou um número válido")
        
def soma(x,y):
    return x+y
def subtracao(x,y):
    return x-y
def multiplicacao(x,y):
    return x*y
def divisao(x,y):
    return x/y

            


if __name__ == '__main__':
    cprint('Hello, World!', 'teste')
    print('Hello, World!', 'teste')
    