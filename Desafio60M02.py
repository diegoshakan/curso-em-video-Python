from math import factorial
'''Crie um programa que mostre o fatorial de qualquer número solicitado.'''

'''
# Está é a forma braçal rsrs
fat = 1
cont = 1
num = int(input('Qual número você deseja fatorar: '))

for c in range(num):
    fat = fat * cont
    cont += 1
print(f'O fatorial de {num} é = {fat}')'''

num = int(input('Qual número você deseja fatorar: '))
print(f'O fatorial de {num} é = {factorial(num)}')