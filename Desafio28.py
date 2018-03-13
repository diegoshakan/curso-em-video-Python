import random

'''Faça um programa em que o computador "pensa" em número, e receba um número do usuário e diga
se ele acertou ou não.'''

num = random.randint(0, 5)

palp = int(input('Diga o número que estou pensando: '))

if num == palp:
    print('Acertô miseravi! rsrs')
else:
    print('Errou feio!')
