'''Refaça o Desafio 35, acrescente que tipo de triângulo será formado:
Equilátero: Todos os lados iguais.
Isóceles: Dois lados iguais.
Escaleno: Todos os lados diferentes.
'''

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print('As retas podem formar um triângulo.')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Formam um triângulo EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Formam um triângulo ISÓCELES.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Formam um triângulo ESCALENO.')
else:
    print('As retas acima não podem formar um triângulo')


