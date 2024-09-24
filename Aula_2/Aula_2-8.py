'''
Exercício 08: Calcule o seno, cosseno e tangente, em graus e radianos 
de 45°, 60°, 90°, 180°, 270°, 360°
'''
from math import sin, cos, tan, radians
def trigonometria(angulos):
    for angulo in angulos:
        print(f'{angulo}°')
        print(f'Seno: {sin(angulo)}\nCosseno: {cos(angulo)}\nTangente: {tan(angulo)}')
        print(f'Seno rad: {sin(radians(angulo))}\nCosseno rad: {cos(radians(angulo))}\nTangente rad: {tan(radians(angulo))}')
        print('-'*30)
    
trigonometria([45,60,90,180,270,360])