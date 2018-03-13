import random

'''Faça um programa que sorteie o nome de quatro alunos e mostre o sorteado.'''

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

l = [nome1, nome2, nome3, nome4]

print('O aluno escolhido foi {}'.format(random.choice(l)))