from datetime import date

'''Faça um programa que leia o ano de nascimento e diga se:

- Ele ainda vai se alistar ao serviço militar.
- Está na hora de se alistar.
- Já passou do tempo de se alistar.

Seu programa tem que mostrar quanto tempo falta para se alistar ou quanto tempo já passou do prazo.
'''

nasc = int(input('Qual é o seu ano de nascimento: '))
ano = date.today().year

idade = ano - nasc
fal = 18 - idade
pas = idade - 18

if idade < 18:
    print('Você ainda não pode se alistar, sua idade {} anos e faltam {} ano(s) para se alistar.'.format(idade, fal))
elif idade > 18:
    print('Você passou da idade do alistamento, se apresente a junta militar da sua cidade. sua idade {} anos e você atrasou {} ano(s).'.format(idade, pas))
else:
    print('Você está no ano de alistamento, compareça a junta da sua cidade.')