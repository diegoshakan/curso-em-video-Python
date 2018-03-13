#Desafio 22 - Gustavo Guanabara

'''Crie um programa que leia o nome completo de uma pessoa e mostre:
a) O nome com todas as letras maiúsculas:
b) O nome com todas minúsculas:
c) Quantas letras ao todo sem considerar o espaço:
d) Quantas letras tem o primeiro nome:'''

#a)
nome = input('Escreva seu nome: ')
nome = nome.upper() #Aqui ele deixa tudo maiúsculo
print(nome)

#b)
nome = input('Escreva seu nome: ')
nome = nome.lower() #Aqui ele deixa tudo minúsculo.
print(nome)

#c)
nome = input('Escreva seu nome: ').strip() #.strip serve para retirar todos os espaços antes e/ou após a string.
nome1 = nome.count(' ') #aqui ele conta qnts espaços há na frase em outra variável.
nome = len(nome) - nome1 #Aqui ele calcula a qntd de caracteres e diminui pela qntd de espaços, dando o total de letras apenas.
print('Seu nome completo tem {} letras'.format(nome)) #aqui ele imprime o nome formatado com o cálculo.

#d)
nome = input('Escreva seu nome: ')
nome = nome.split() #aqui separa o nome completo
nome = len(nome[0]) #aqui confere quantas letras há no primeiro nome somente.
print('Seu primeiro nome tem {} letras'.format(nome))