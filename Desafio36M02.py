'''Faça um programa para aprovar um empréstimo bancário para a compra de uma casa.
O programa irá perguntar o valor da casa, o salário do comprador e em quantos anos ele pretende pagar.
Calcule o valor da prestação mensal, visando não ultrapassar 30% do valor do salário, ou então o
empréstimo será negado.'''

casa = float(input('Valor da casa: '))
sal = float(input('Qual é o seu salário: '))
prazo = int(input('Quantos anos pretende pagar: '))

meses = prazo * 12

fin = casa / meses

sal = sal * 0.3

if fin <= sal:
    print('Seu financiamento foi aprovado! Sua parcela será R$ {:.2f} mensal.'.format(fin))
elif fin > sal:
    print('Seu financiamento foi negado!')