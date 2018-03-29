from time import sleep
from datetime import date
'''Faça um programa que mostra na tela uma contagem regressiva para estouros de fogos de 10 até 0.'''

for c in range (10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO {}!'.format(date.today().year + 1))