'''Faça um programa que leia um valor de um produto e apresente um preço com 5% de desconto.'''

val = float(input('Qual o valor da mercadoria: '))
desc = val - (val * 5/100)
print('Seu valor com desconto de 5% é: R$ {:.2f}'.format(desc))