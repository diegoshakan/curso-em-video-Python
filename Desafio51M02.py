'''Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética.
No final mostre os 10 primeiros termos desta progressão.'''

ter = int(input('Digite o termo da P. A.: '))
raz = int(input('Digite a razão da P. A.: '))
ene = ter + (10 - 1) * raz

for c in range(ter, ene + 1, raz):
    print('=> {}'.format(c))