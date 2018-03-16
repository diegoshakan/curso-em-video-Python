import datetime

'''Faça um programa que leia um ano e mostre se ele é bissexto.'''

ano = int(input('Digite um ano: '))


if ano == 0:
    ano = datetime.date.today().year
if ano % 400 == 0 or ano % 100 != 0 and ano % 4 == 0:
    print('{} é Bissexto'.format(ano))
else:
    print('{} não é Bissexto'.format(ano))