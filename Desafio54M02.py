from datetime import date

'''Crie um programa que leia o ano de nascimento de sete pessoas e mostre quantass já atingiram
a maioridade e quantas ainda não.'''

menor = 0
maior = 0
hoje = date.today().year


for c in range(0, 7):
    data = int(input('Digite o ano de nascimento: '))
    if hoje - data < 21:
        menor += 1
    elif hoje - data >= 21:
        maior += 1
print('{} São (é) menor(es) de idade.'.format(menor))
print('{} São (é) maior(es) de idade.'.format(maior))