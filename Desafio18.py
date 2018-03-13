import math
'''Faça um programa que leia um ângulo e mostre o Seno, Cosseno e Tangente desse ângulo.'''

ang = int(input("Digite o ângulo: "))
print('Seno: {:.3f}'.format(math.sin(math.radians(ang))))
print('Cosseno: {:.3f}'.format(math.cos(math.radians(ang))))
print('Tangente: {:.3f}'.format(math.tan(math.radians(ang))))