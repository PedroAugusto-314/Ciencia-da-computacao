"""
7) Faça um programa que:
a) Mostre todas as combinações possíveis entre 1, 2 e 3, de tamanho 3
b) Mostre todas as combinações possíveis entre 1, 2, 3 e 4, de tamanho 4
c) Mostre todas as combinações possíveis entre 1, 2, 3, 4 e 5, de tamanho 5
d) Mostre todas as combinações possíveis entre 1, 2, 3, 4, 5, 6, de tamanho 6
e) Mostre todas as combinações possíveis entre 1, 2, 3, 4, 5 ,6 ,7, de tamanho 7
"""
def analise_combinatoria(num_list : list, lenght : int) -> int:
    num_list.sort()
    high_num = num_list[-1]  
    if 0 in num_list: high_num += 1
    return high_num**lenght

#a)
for x in range(1,4):
    for y in range(1,4):
        for z in range(1,4):
            print(x,y,z)


  
def combinacoes(lista, tamanho):
    if tamanho < 1:
        return 
    else:
        for i in range(1,len(lista)+1):
            combinacoes(lista, tamanho-1)

