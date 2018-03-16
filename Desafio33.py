'''Faça um programa que leia três números e mostre qual deles é o maior e o menor'''

a = int(input('1º Número: '))
b = int(input('2º Número: '))
c = int(input('3º Número: '))

if a < b and a < c:
    print('O número {} é o menor.'.format(a))
elif b < a and b < c:
    print('O número {} é o menor.'.format(b))
else:
    print('O número {} é o menor.'.format(c))

if a > b and a > c:
    print('O número {} é o maior.'.format(a))
elif b > a and b > c:
    print('O número {} é o maior.'.format(b))
else:
    print('O número {} é o maior.'.format(c))