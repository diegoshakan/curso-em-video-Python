#Desafio 25 - Gustavo Guanabara
'''Crie um programa que leia um nome de pessoa e diga se tem SILVA no nome'''

nome = input('Diga seu nome: ').split()
nome1 = nome.lower().find('silva') #Aqui coloca tudo minúsculo e procura a posição onde se inicia o nome procurado.
if nome1 >= 0: #Como o .find() localiza a posição, se existe é maior ou igual a 0, se não existe sempre mostra -1, pude fazer essa comparação.
    print('Seu nome tem \"SILVA\"')
else:
    print('Seu nome não tem \"SILVA\"')

#print(nome1) #se você quiser testar é só imprimir um nome com ou sem silva,
# e mostrará -1 se não tiver, e um número igual ou acima de 0 se exisir Silva no nome.
