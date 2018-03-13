'''Faça um programa que leia um número e mostre o seu antecessor e seu sucessor.'''

a = int(input('Digite um número: '))

ant = a - 1
suc = a + 1

print('O número escolhido foi {}, seu antecessor é {} e o sucessor é {}'.format(a, ant, suc))