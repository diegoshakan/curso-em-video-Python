'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
se elas podem ou não formar um triângulo.'''

a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))

r1 = abs(b - c) < a < b + c  # abs() mostra o módulo de um número, operação.
r2 = abs(a - c) < b < a + c
r3 = abs(a - b) < c < a + b

if r1 == True and r2 == True and r3 == True:
    print('Forma um triângulo.')
else:
    print('Não forma um triângulo.')
