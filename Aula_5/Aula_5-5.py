"""
5) Você esta num consórcio entre amigos no valor de R$ 100,00, com 10 participantes. Faça um algoritmo 
que, usando o comando “for”, calcule qual o valor final que você irá receber, sabendo que sua cota é a 
última e a partir do segundo mês, o valor é reajustado em 2%.
Valor = R$ 100,00
Quantidade de meses = 10
1˚ mês: 100,00 * 10 = 1000,00
2˚ mês: (100 * 1.02) * 10 = 102 * 10 = 1020,00
3˚ mês: (102 * 1.02) * 10 = 104,04 * 10 = 1040,04
"""
valor : int = 100
for i in range(1, 11):
    juros = 1.02 if i > 1 else 1
    valor *= juros
    print(f'{i}° Mês: R${valor*10:.2f}')
