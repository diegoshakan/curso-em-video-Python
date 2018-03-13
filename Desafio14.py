'''Crie um programa de conversão de temperatura de Celsius para Fahrenheit'''

temp = float(input('Insira a temperatura em Celsius para conversão em Fahrenheit: '))

f = 1.8 * temp + 32
#f = 9 * temp / 5 +32

print('A temperatura em Fahrenheit é {:.1f}⁰'.format(f))