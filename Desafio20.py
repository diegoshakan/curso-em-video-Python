import random

'''Faça um programa que embaralhe os nomes de quatro alunos, e mostre uma nova sequência.'''

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

nomes = [nome1, nome2, nome3, nome4]

random.shuffle(nomes)
print('Está será a ordem de apresentação {}'.format(nomes))
