'''Faça um programa que leia um algo pelo teclado e mostre na tela seu tipo primitivo e
todas as informações possíveis sobre ele'''

a = input('Digite algo: ')

print('Este tipo é ', type(a))
print('Somente números: ', a.isnumeric())
print('Somente letras: ', a.isalpha())
print('É alfanumerico: ', a.isalnum())
print('Está em minúsculo:', a.islower())

#com estes métodos (*.iscapitalize(), *.istitle(), etc.)podemos ter várias outras informações.