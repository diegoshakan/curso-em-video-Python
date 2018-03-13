#from math import sqrt '''Para fazer a raiz quadrada, outra forma'''

'''Crie um algorítmo que leia um número e mostre seu dobro, seu triplo e a raiz quadrada'''

a = int(input('Digite um número: '))

d = a * 2
t = a * 3
r = a ** (1/2)
#r = sqrt(a) outra forma de se fazer a raiz quadrada

print('Dobro: {}, Triplo: {}, Raiz Quadrada: {:.1f}'.format(d, t, r))