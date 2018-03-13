from math import sqrt
from math import hypot

'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, e
mostre o valor do comprimento da hipotenusa.'''

catopo = float(input('Cateto Oposto: '))
catadj = float(input('Cateto Adjacente: '))

#hip = hypot(catopo, catadj) #Método que já faz o cálculo direto da hipotenusa
#hip = sqrt(catopo ** 2 + catadj ** 2) #Método que faz a raiz quadrada.
hip = (catopo ** 2 + catadj ** 2) ** (1/2) #Algorítmo sem precisa importar métodos.

print('O valor da hipotenusa é: {:.2f}'.format(hip))