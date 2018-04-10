'''Crie um programa que leia uma frase qualquer e diga se é um palíndromo, desconsiderando os
espaços.'''

nome = input('Digite uma frase: ').strip().lower()
nome = nome.replace(' ', '')
nomeAoContrario = nome[::-1].lower()
if nome == nomeAoContrario:
   print('{} e {} é palíndromo!'.format(nome, nomeAoContrario))
else:
   print('{} e {} Não é palíndromo!'.format(nome,nomeAoContrario))

'''Não consegui fazer com FOR, muito arrodeio kkkkk'''


