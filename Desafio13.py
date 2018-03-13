'''Faça um algorítmo que leia o salário de um funcionário e o mostre com aumento de 15%'''

sal = float(input('Qual é o seu salário: '))

aum = (sal * 0.15) + sal

print('Parabéns, seu novo salário é R$ {:.2f}'.format(aum))