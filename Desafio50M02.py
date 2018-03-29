'''Desenvolva um programa que leia seis números inteiros e mostre a soma somente daqueles
que forem pares. Os ímpares, são descartados.'''

soma = 0

for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
print(soma)