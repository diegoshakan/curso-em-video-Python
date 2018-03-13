#Desafio27 - Gustavo Guanabara
'''Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o último nome
dela'''

nome = input('Digite seu nome completo: ').title().strip()
nome = nome.split()
nomeFinal = len(nome)
nomeFinal1 = nomeFinal - 1
print('Primeiro nome: {}'.format(nome[0]))
print('Último nome: {}'.format(nome[nomeFinal1]))



