'''Escreva um programa que leia dois números inteiros e os compare, mostrando na tela as seguintes
frases:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
'''

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

if a > b:
    print('O primeiro valor é maior.')
elif b > a:
    print('O segundo valor é maior.')
else:
    print('Os dois valores são iguais.')
