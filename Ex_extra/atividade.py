import os
import dec_bin

#Binário para decimal
os.system('cls')


num_bin = dec_bin.convert_bin_dec(input("Digite um número binário para converter para decimal: "))
print(f"Conversão: {num_bin}")




#Decimal para binário


####Chatgpt--> como levantar excessões na função
# def executar_comando(comando):
#     if not isinstance(comando, str):  # Verifica se 'comando' é uma string
#         raise ValueError("O argumento deve ser uma string.")  # Levanta um erro se não for
#     os.system(comando)  # Executa o comando se a verificação passar
