'''Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a
base de conversão.
1 - Binário
2 - Octal
3 - Hexadecimal'''

cod = int(input('Escolha um número para realizar a conversão: 1 - Binário, 2 - Octal ou 3 - Hexadecimal: '))
num = int(input('Qual número inteiro você quer converter: '))

if cod == 1:
    print(bin(num)[2:])
elif cod == 2:
    print(oct(num)[2:])
elif cod == 3:
    print(hex(num)[2:])
else:
    print('Código inexistente!')