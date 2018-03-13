import math

'''Crie um programa que receba um número real do usuário e mostre apenas a parte inteira do número.
Ex: Nº Real:        23.456
Parte Inteira:      23
'''

a = float(input('Digite um número real: '))
b = a // 1
#b = math.trunc(a)
#b = int(a)
print('A parte inteira do seu número é {:.0f}'.format(b))