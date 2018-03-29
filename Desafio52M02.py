'''Faça um programa que leia um número inteiro e diga se ele é ou não é um número primo.'''

num = int(input('Digite um número: '))
cont = 0

for c in range(1, num + 1):
    primo = num % c == 0

    if primo is True:
        cont = cont + 1
if cont == 2:
    print('{} é um número primo.'.format(num))
else:
    print('{} não é um número primo.'.format(num))