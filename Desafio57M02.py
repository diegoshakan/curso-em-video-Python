'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F', caso esteja
errado, peça a digitação até ter uma entrada correta.'''

sexo = input('Qual é o seu sexo [M/F]: ').strip().upper()

while sexo not in 'MF':
    sexo = input('Digite novamente, apenas [M/F]:').strip().upper()