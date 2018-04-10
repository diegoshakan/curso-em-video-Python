'''Faça um programa que leia o peso de cinco pessoas e no final diga qual foi o maior e o menor
peso lido.'''

lista = []
for p in range(0, 5):
    peso = float(input('Digite o peso: '))
    lista.append(peso) # ".append" adiciona o valor ao índice.
print('O maior peso é {}Kg'.format(max(lista))) # "max()" mostra o maior valor do índice.
print('O menor peso é {}Kg' .format(min(lista))) # "min()" mostra o menor valor do índice.

'''
exemplo:
lista = [1, 2, 3, 4, 5]
print(min(lista)) #aqui o resultado será 1
print(max(lista)) #aqui o resultado será 5
'''