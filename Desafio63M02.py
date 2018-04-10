'''Crie um programa que gere 'n' termos da sequência Fibonacci'''

ant, pos = 1, 0
num = int(input('Quantos termos da sequência Fibonacci você deseja: '))
print(0, end=' ')
for c in range(1, num):
    prox = pos + ant
    ant = pos
    pos = prox
    print(prox, end=' ')