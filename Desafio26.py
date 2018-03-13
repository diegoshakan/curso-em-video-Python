# Desafio 26 - Gustavo Guanabara
'''Crie um programa que leia uma frase pelo teclado e diga:
a) Quantas vezes aparece a letra 'a':
b) Em que posição ela aparece a primeira vez:
c) Em que posição ela aparece a última vez:
'''

frase = input('Digite uma frase: ').strip()
frase1 = frase.lower().count('a')
print('Há {} letras \"A\" na frase'.format(frase1))
print('A primeira letra \"A\" aparece na posição {}'.format(frase.find('a') + 1))
print('A última letra \"A\" aparece na posição {}'.format(frase.rfind('a') + 1))

